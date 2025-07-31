from typing import List
from collections import defaultdict, Counter
import math

"""
You are building a lightweight system to track user visits to GPS coordinates and query which users were near a location.
"""


class LocationTracker:
    def __init__(self):
        # Initialize your data structures
        self.storage = defaultdict(list)

    def log_visit(self, user_id: str, lat: float, lon: float, timestamp: str) -> None:
        # Log a user visit to a lat/lon with a timestamp
        assert all(v is not None for v in [user_id, lat, lon, timestamp])
        self.storage[user_id].append((lat, lon, timestamp))

    def get_users_near(self, lat: float, lon: float, radius_km: float) -> List[str]:
        # Return list of unique user_ids who visited within radius_km of given point
        # Use approximate flat-Earth distance: sqrt((lat1-lat2)^2 + (lon1-lon2)^2) * 111 ≈ km

        result = set()

        for user_id, visits in self.storage.items():
            for new_lat, new_lon, _ in visits:
                dist = math.sqrt(pow((lat - new_lat), 2) + pow((lon - new_lon), 2)) * 111
                if dist <= radius_km:
                    result.add(user_id)
                    break

        return list(result)


if __name__ == '__main__':
    lt = LocationTracker()
    lt.log_visit("alice", 37.77, -122.42, "2024-07-01T10:00:00")
    lt.log_visit("bob", 37.76, -122.41, "2024-07-01T10:05:00")
    lt.log_visit("charlie", 38.0, -123.0, "2024-07-01T10:10:00")

    assert set(lt.get_users_near(37.77, -122.42, 2)) == {"alice", "bob"}
    assert set(lt.get_users_near(38.0, -123.0, 1)) == {"charlie"}
    assert set(lt.get_users_near(36.0, -120.0, 10)) == set()


# V2

import math
from typing import List
from collections import defaultdict, Counter


"""
You are building a lightweight system to track user visits to GPS coordinates and query which users were near a location.
"""


class LocationTracker:
    def __init__(self):
        self.storage = defaultdict(list)

    def log_visit(self, user_id: str, lat: float, lon: float, timestamp: str) -> None:
        """
        Log a visit by a user to a specific GPS coordinate at a specific time.
        """
        assert all(v is not None for v in [user_id, lat, lon, timestamp])

        self.storage[user_id].append([lat, lon, timestamp])
        print(self.storage)

    def get_users_near(self, lat: float, lon: float, radius_km: float) -> list[str]:
        """
        Return a list of user_ids who have visited within radius_km of the given location.
        """

        assert all(v is not None for v in [lat, lon, radius_km])

        # Should be populated
        result = []

        for user_id, data in self.storage.items():
            for lat1, lon1, _ in data:
                new_dist = math.sqrt(pow(lat-lat1, 2) + pow(lon-lon1, 2)) * 111

                if new_dist <= radius_km:
                    result.append(user_id)

        return result



if __name__ == '__main__':
    lt = LocationTracker()
    lt.log_visit("alice", 37.77, -122.42, "2024-07-01T10:00:00")
    lt.log_visit("bob", 37.76, -122.41, "2024-07-01T10:05:00")
    lt.log_visit("charlie", 38.0, -123.0, "2024-07-01T10:10:00")

    assert set(lt.get_users_near(37.77, -122.42, 2)) == {"alice", "bob"}
    assert set(lt.get_users_near(38.0, -123.0, 1)) == {"charlie"}
    assert set(lt.get_users_near(36.0, -120.0, 10)) == set()
