import math
import json
import unittest
from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

"""
Constraints:
1. Use the haversine formula to compute distance.
2. Only include check-ins that happened within 10 minutes before the given timestamp.
3. You may assume check-ins are not sorted.
4. Optimize for frequent queries.
"""


class ProximityTracker:
    def __init__(self):
        self.check_ins = defaultdict(list)

    def haversine(self, lat1, lon1, lat2, lon2):

        R = 6371
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def check_in(self, user_id, lat, lon, timestamp):

        assert all(v is not None for v in [user_id, lat, lon, timestamp])
        # O(1)
        self.check_ins[user_id].append((lat, lon, timestamp))

    def query_nearby(self, lat, lon, radius_km, timestamp):

        assert all(v is not None for v in [lat, lon, radius_km, timestamp])
        result = set()

        for uid, data in self.check_ins.items():
            for lat1, lon1, ts in data:
                dist = self.haversine(lat1, lon1, lat, lon)
                upper_bound = datetime.fromisoformat(timestamp)
                time_window = datetime.fromisoformat(timestamp) - timedelta(minutes=10)
                checkin_time = datetime.fromisoformat(ts)
                if dist <= radius_km and time_window <= checkin_time <= upper_bound:
                    result.add(uid)

        return list(result)


# V2
"""
💬 Challenge Description
Build a real-time spatial check-in engine with time filtering and spatial indexing.

Requirements: Design a class SpatialIndexer with two main methods: 
1. ingest(data: List[Dict]): Accepts a list of 
check-in dicts (user_id, lat, lon, timestamp). 
2. query(lat: float, lon: float, radius_km: float, timestamp: str) -> 
List[str]: Returns list of user IDs that checked in within radius_km and within 10 minutes before the query 
timestamp.

Constraints:
1. Use the haversine formula to compute distance. + 
2. Optimize for frequent queries (avoid brute-force).
3. Use spatial grid partitioning (defaultdict by coordinate cell).
4. Time filtering must happen after spatial pruning
"""


class SpatialIndexer:
    def __init__(self, scale: int = 100):
        # TODO: Init your spatial grid here (e.g., defaultdict)
        self.scale = scale
        self.checkins = defaultdict(list)
        self.cache = defaultdict(list)

    def haversine(self, lat1, lon1, lat2, lon2):

        R = 6371
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def __get_cell__(self, lat, lon):
        return int(lat * self.scale), int(lon * self.scale)

    def ingest(self, data: List[Dict[str, Any]]) -> None:
        # TODO: Process check-ins into the appropriate grid cells
        assert (data is not None), "Data is empty"

        """
        1. Parse the data
        2. Confirm all fields exist
        3. Convert ts using datetime
        4. Optimize
        """

        for entry in data:
            ts: datetime = datetime.fromisoformat(entry['timestamp'])
            # self.checkins[entry['user_id']].append((entry['lat'], entry['lon'], ts))
            cell = self.__get_cell__(entry['lat'], entry['lon'])
            self.checkins[cell].append((entry['user_id'], entry['lat'], entry['lon'], ts))

        print(self.checkins)

    def query(self, lat: float, lon: float, radius_km: float, timestamp: str) -> List[str]:
        
        assert all(v is not None for v in [lat, lon, radius_km, timestamp])

        uid = f"{lat:.6f}_{lon:.6f}_{timestamp}"
        if uid in self.cache:
            return self.cache[uid]

        result = set()
        center_cell = self.__get_cell__(lat, lon)
        neighbor_offsets = [-1, 0, 1]

        upper_bound = datetime.fromisoformat(timestamp)
        time_window = upper_bound - timedelta(minutes=10)

        for dx in neighbor_offsets:
            for dy in neighbor_offsets:
                cell = (center_cell[0] + dx, center_cell[1] + dy)
                for user_id, lat1, lon1, ts in self.checkins.get(cell, []):
                    dist = self.haversine(lat, lon, lat1, lon1)
                    if dist <= radius_km and time_window <= ts <= upper_bound:
                        result.add(user_id)

        r = sorted(result)
        self.cache[uid] = r
        return r


class TestSpatialIndexer(unittest.TestCase):

    def setUp(self):
        self.indexer = SpatialIndexer()

        # Sample check-ins
        self.checkins = [
            {"user_id": "alice", "lat": 37.77, "lon": -122.42, "timestamp": "2025-07-31T10:00:00"},
            {"user_id": "bob", "lat": 37.775, "lon": -122.418, "timestamp": "2025-07-31T10:08:00"},
            {"user_id": "charlie", "lat": 37.5, "lon": -122.0, "timestamp": "2025-07-31T09:45:00"},
            {"user_id": "dana", "lat": 37.771, "lon": -122.421, "timestamp": "2025-07-31T10:02:00"},
            {"user_id": "ed", "lat": 37.88, "lon": -122.5, "timestamp": "2025-07-31T10:06:00"},
            {"user_id": "alice", "lat": 37.77, "lon": -122.42, "timestamp": "2025-07-31T09:55:00"}
        ]
        self.indexer.ingest(self.checkins)

    def test_nearby_users_basic(self):
        query = {
            "lat": 37.77,
            "lon": -122.42,
            "radius_km": 1.0,
            "timestamp": "2025-07-31T10:10:00"
        }
        result = self.indexer.query(**query)
        self.assertCountEqual(result, ["alice", "bob", "dana"])

    def test_time_filtering(self):
        # This should not return "charlie" because timestamp too early
        query = {
            "lat": 37.5,
            "lon": -122.0,
            "radius_km": 1.0,
            "timestamp": "2025-07-31T10:10:00"
        }
        result = self.indexer.query(**query)
        self.assertCountEqual(result, [])  # Outside 10-minute window

    def test_distance_filtering(self):
        # Should exclude ed (too far away)
        query = {
            "lat": 37.77,
            "lon": -122.42,
            "radius_km": 0.5,
            "timestamp": "2025-07-31T10:10:00"
        }
        result = self.indexer.query(**query)
        self.assertNotIn("ed", result)

    def test_query_caching(self):
        query = {
            "lat": 37.77,
            "lon": -122.42,
            "radius_km": 1.0,
            "timestamp": "2025-07-31T10:10:00"
        }
        first = self.indexer.query(**query)
        second = self.indexer.query(**query)
        self.assertEqual(first, second)

        expected_cache_key = f"{query['lat']:.6f}_{query['lon']:.6f}_{query['timestamp']}"
        self.assertIn(expected_cache_key, self.indexer.cache)


if __name__ == '__main__':
    proximity = ProximityTracker()
    proximity.check_in("alice", 37.77, -122.42, "2025-07-31T10:00:00")
    proximity.check_in("bob", 37.775, -122.418, "2025-07-31T10:08:00")
    proximity.check_in("charlie", 37.5, -122.0, "2025-07-31T09:45:00")

    results = proximity.query_nearby(37.77, -122.42, 1.0, "2025-07-31T10:10:00")
    # Should return ['alice', 'bob']

    checkins = [
        {"user_id": "alice", "lat": 37.77, "lon": -122.42, "timestamp": "2025-07-31T10:00:00"},
        {"user_id": "bob", "lat": 37.775, "lon": -122.418, "timestamp": "2025-07-31T10:08:00"},
        {"user_id": "charlie", "lat": 37.5, "lon": -122.0, "timestamp": "2025-07-31T09:45:00"},
        {"user_id": "dana", "lat": 37.771, "lon": -122.421, "timestamp": "2025-07-31T10:02:00"},
        {"user_id": "ed", "lat": 37.88, "lon": -122.5, "timestamp": "2025-07-31T10:06:00"},
        {"user_id": "alice", "lat": 37.77, "lon": -122.42, "timestamp": "2025-07-31T09:55:00"}
    ]

    with open('checkins.json', 'w') as f:
        json.dump(checkins, f, indent=2)

    # ["alice", "bob", "dana"]
    query = {
        "lat": 37.77,
        "lon": -122.42,
        "radius_km": 1.0,
        "timestamp": "2025-07-31T10:10:00"
    }

    with open('checkins.json', 'r') as f:
        data = json.load(f)

    indexer = SpatialIndexer()
    indexer.ingest(data)
    indexer.query(**query)
    unittest.main()
