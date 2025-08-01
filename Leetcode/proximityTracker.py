import math
from collections import defaultdict
from datetime import datetime, timedelta


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


if __name__ == '__main__':
    proximity = ProximityTracker()
    proximity.check_in("alice", 37.77, -122.42, "2025-07-31T10:00:00")
    proximity.check_in("bob", 37.775, -122.418, "2025-07-31T10:08:00")
    proximity.check_in("charlie", 37.5, -122.0, "2025-07-31T09:45:00")

    results = proximity.query_nearby(37.77, -122.42, 1.0, "2025-07-31T10:10:00")
    # Should return ['alice', 'bob']
