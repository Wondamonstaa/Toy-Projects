import math
from datetime import datetime
from typing import List, Dict, Optional
from collections import defaultdict, Counter

"""
You are building a lightweight system to track user visits to GPS coordinates and query which users were near a location.
"""


class LocationTracker:
    def __init__(self, scale=100):
        self.storage = defaultdict(list)

        # Spatial grid implementation: key = (cell_x, cell_y) → list of (user_id, lat, lon, timestamp)
        self.grid = defaultdict(list)
        self.scale = scale

    def __get_cell__(self, lat, lon):
        return (int(lat * self.scale), int(lon * self.scale))

    def log_visit(self, user_id: str, lat: float, lon: float, timestamp: str) -> None:
        """
        Log a visit by a user to a specific GPS coordinate at a specific time.
        """
        assert all(v is not None for v in [user_id, lat, lon, timestamp])

        cell = self.__get_cell__(lat, lon)
        self.grid[cell].append((user_id, lat, lon, timestamp))

    def get_users_near(self, lat: float, lon: float, radius_km: float) -> list[str]:
        """
        Return a list of user_ids who have visited within radius_km of the given location.
        """

        assert all(v is not None for v in [lat, lon, radius_km])

        result = set()
        center_cell = self.__get_cell__(lat, lon)
        neighbor_offsets = [-1, 0, 1]

        for dx in neighbor_offsets:
            for dy in neighbor_offsets:
                cell = (center_cell[0] + dx, center_cell[1] + dy)
                for user_id, lat1, lon1, _ in self.grid.get(cell, []):
                    dx_km = (lat - lat1) * 111
                    dy_km = (lon - lon1) * 85
                    dist = math.sqrt(math.pow(dx_km, 2) + math.pow(dy_km, 2))

                    if dist <= radius_km:
                        result.add(user_id)

        return list(result)

    def get_users_near_in_time(self, lat, lon, radius_km, start_time: str, end_time: str) -> list[str]:

        assert all(v is not None for v in [lat, lon, radius_km, start_time, end_time]), "Some values are None."

        result = set()

        start_time_iso = datetime.fromisoformat(start_time)
        end_time_iso = datetime.fromisoformat(end_time)
        center_cell = self.__get_cell__(lat, lon)
        neighbor_offsets = [-1, 0, 1]

        for dx in neighbor_offsets:
            for dy in neighbor_offsets:
                cell = (center_cell[0] + dx, center_cell[1] + dy)
                for user_id, lat1, lon1, ts in self.grid.get(cell, []):
                    dx_km = (lat - lat1) * 111
                    dy_km = (lon - lon1) * 85
                    dist = math.sqrt(math.pow(dx_km, 2) + math.pow(dy_km, 2))
                    ts = datetime.fromisoformat(ts)

                    if dist <= radius_km and start_time_iso <= ts <= end_time_iso:
                        result.add(user_id)

        return list(result)

    def get_most_visited_cell(self, start_time: str, end_time: str) -> Optional[tuple[float, float]]:

        assert all(v is not None for v in [start_time, end_time])

        """
        Iterate over all grid cells.
        Count how many visits each cell had within the given time range.
        Return the (lat, lon) center point of the cell with the most visits in that range.
        If multiple cells tie, return any of them.
        
        lat_center = x / self.scale
        lon_center = y / self.scale
        """

        max_count = 0
        best_cell = None
        start_time_iso = datetime.fromisoformat(start_time)
        end_time_iso = datetime.fromisoformat(end_time)

        for (x,y), visits in self.grid.items():
            count = 0
            for user_id, lat, lon, ts in visits:
                ts = datetime.fromisoformat(ts)
                if start_time_iso <= ts <= end_time_iso:
                    count += 1
            if count > max_count:
                max_count = count
                best_cell = (x, y)

        if best_cell is None:
            return None

        lat_center = best_cell[0] / self.scale
        lon_center = best_cell[1] / self.scale

        return lat_center, lon_center


# ES Simulation test
class ElasticSim:
    def __init__(self):
        self.documents = []  # Simulates Elasticsearch index

    def index_visit(self, user_id: str, lat: float, lon: float, timestamp: str) -> None:
        self.documents.append({
            "user_id": user_id,
            "lat": lat,
            "lon": lon,
            "timestamp": datetime.fromisoformat(timestamp),
        })

    def query_visits(self, lat: float, lon: float, radius_km: float,
                     start_time: str, end_time: str) -> List[Dict]:
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)

        # Approximate geo-distance filter
        def is_within_radius(doc):
            d = math.sqrt((lat - doc["lat"]) ** 2 + (lon - doc["lon"]) ** 2) * 111
            return d <= radius_km

        return [
            doc for doc in self.documents
            if start_dt <= doc["timestamp"] <= end_dt and is_within_radius(doc)
        ]

    def most_visited_cell(self, scale: int, start_time: str, end_time: str) -> Optional[tuple[float, float]]:
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)
        cell_counter = defaultdict(int)

        for doc in self.documents:
            if start_dt <= doc["timestamp"] <= end_dt:
                x = int(doc["lat"] * scale)
                y = int(doc["lon"] * scale)
                cell_counter[(x, y)] += 1

        if not cell_counter:
            return None

        best_cell = max(cell_counter.items(), key=lambda item: item[1])[0]
        return (best_cell[0] / scale, best_cell[1] / scale)



if __name__ == '__main__':
    lt = LocationTracker()

    lt.log_visit("alice", 37.77, -122.42, "2024-07-01T10:00:00")
    lt.log_visit("bob", 37.76, -122.41, "2024-07-01T10:05:00")
    lt.log_visit("charlie", 38.0, -123.0, "2024-07-01T10:10:00")

    assert set(lt.get_users_near(37.77, -122.42, 2)) == {"alice", "bob"}
    assert set(lt.get_users_near(38.0, -123.0, 1)) == {"charlie"}
    assert set(lt.get_users_near(36.0, -120.0, 10)) == set()

    assert(lt.get_users_near_in_time(37.77, -122.42, 2, "2024-07-01T10:00:00", "2024-07-04T10:00:00"))

    lt.get_users_near_in_time(
        lat=37.77,
        lon=-122.42,
        radius_km=2,
        start_time="2024-07-01T09:00:00",
        end_time="2024-07-01T10:05:00"
    )

    test = lt.get_most_visited_cell(
        start_time="2024-07-01T09:00:00",
        end_time="2024-07-01T10:05:00"
    )

    es = ElasticSim()
    es.index_visit("alice", 37.77, -122.42, "2024-07-01T10:00:00")
    es.index_visit("bob", 37.76, -122.41, "2024-07-01T10:05:00")
    es.index_visit("charlie", 38.0, -123.0, "2024-07-01T10:10:00")

    results = es.query_visits(37.77, -122.42, 2, "2024-07-01T09:00:00", "2024-07-01T11:00:00")
    assert {doc['user_id'] for doc in results} == {"alice", "bob"}

    assert es.most_visited_cell(scale=100, start_time="2024-07-01T09:00:00", end_time="2024-07-01T11:00:00") == (
    37.77, -122.42)
