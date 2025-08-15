from collections import defaultdict
from datetime import datetime


def optimize_deliveries(deliveries):
    working_start = datetime.strptime("8:00", "%H:%M").time()
    working_end = datetime.strptime("18:00", "%H:%M").time()
    filtered = defaultdict(list)

    for entry in deliveries:
        start_time = datetime.strptime(entry["window"][0], "%H:%M").time()

        if working_start <= start_time <= working_end:
            filtered[entry["city"]].append(entry)

    for city in filtered:
        filtered[city] = sorted(
            filtered[city],
            key=lambda x: (-x["priority"], x["window"][0])
        )

    return dict(filtered)


# -----------------------
# Test cases
# -----------------------
def run_tests():
    deliveries = [
        {"city": "Chicago", "window": ["09:00", "10:30"], "priority": 3},
        {"city": "Boston", "window": ["07:00", "09:00"], "priority": 5},  # Out of hours
        {"city": "Chicago", "window": ["11:00", "13:00"], "priority": 2},
        {"city": "Boston", "window": ["15:00", "17:00"], "priority": 1},
        {"city": "Chicago", "window": ["18:30", "19:00"], "priority": 4}  # Out of hours
    ]
    expected = {
        "Chicago": [
            {"city": "Chicago", "window": ["09:00", "10:30"], "priority": 3},
            {"city": "Chicago", "window": ["11:00", "13:00"], "priority": 2}
        ],
        "Boston": [
            {"city": "Boston", "window": ["15:00", "17:00"], "priority": 1}
        ]
    }
    result = optimize_deliveries(deliveries)
    print("Test 1:", result == expected)

    # Additional test — same priority, different start times
    deliveries2 = [
        {"city": "NYC", "window": ["10:00", "11:00"], "priority": 2},
        {"city": "NYC", "window": ["09:00", "09:30"], "priority": 2},
    ]
    expected2 = {
        "NYC": [
            {"city": "NYC", "window": ["09:00", "09:30"], "priority": 2},
            {"city": "NYC", "window": ["10:00", "11:00"], "priority": 2},
        ]
    }
    result2 = optimize_deliveries(deliveries2)
    print("Test 2:", result2 == expected2)


if __name__ == "__main__":
    run_tests()
