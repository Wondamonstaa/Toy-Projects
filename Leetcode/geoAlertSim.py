import math
import datetime
from collections import defaultdict, Counter
from typing import List, Tuple, Dict, Optional, Any

"""
Prompt:

You're building a basic geofencing engine. 
Implement a class that lets you register zones on the map, and detect which users triggered an alert by entering any zone.

Each zone is defined by:
a name (string)
a center point: (lat: float, lon: float)
a radius in kilometers (float)

Each user visit is:
user_id (string)
lat and lon (floats)
timestamp (string ISO8601)
"""


class GeoAlertSystem:

    def __init__(self):
        self.alert_zones = defaultdict(list)
        self.visits = defaultdict(list)

    def add_zone(self, name: str, lat: float, lon: float, radius_km: float) -> None:
        """Registers a new alert zone by name."""
        self.alert_zones[name].append((lat, lon, radius_km))

    def haversine(self, lat1, lon1, lat2, lon2):

        R = 6371
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def log_visit(self, user_id: str, lat: float, lon: float, timestamp: str) -> None:
        """Logs a visit and internally stores any alerts triggered."""

        alert = None

        for zone, data in self.alert_zones.items():
            for lat1, lon1, radius_km in data:
                distance = math.sqrt((lat1 - lat) ** 2 + (lon1 - lon) ** 2) * 111
                # distance = distance = self.haversine(lat1, lon1, lat, lon)
                if distance <= radius_km:
                    alert = zone
                    self.visits[user_id].append((lat, lon, timestamp, alert))

    def get_alerts_for_user(self, user_id: str) -> List[str]:
        """Returns a list of zone names this user triggered."""
        zones = set()

        for uid, data in self.visits.items():
            for lat1, lon1, ts, trigger in data:
                if uid == user_id:
                    zones.add(trigger)

        return list(zones)


if __name__ == '__main__':
    gas = GeoAlertSystem()
    gas.add_zone("school", 37.77, -122.42, 1.0)
    gas.add_zone("hospital", 38.0, -123.0, 2.0)

    gas.log_visit("alice", 37.775, -122.418, "2024-07-01T10:00:00")
    gas.log_visit("bob", 38.01, -123.01, "2024-07-01T10:05:00")
    gas.log_visit("charlie", 36.0, -121.0, "2024-07-01T10:10:00")

    assert set(gas.get_alerts_for_user("alice")) == {"school"}
    assert set(gas.get_alerts_for_user("bob")) == {"hospital"}
    assert gas.get_alerts_for_user("charlie") == []
