from typing import List
from collections import defaultdict, Counter


class PlaceTagger:
    def __init__(self):
        self.storage = {}

    def add_place(self, place_id: str, tags: List[str]) -> None:
        assert place_id is not None and tags is not None
        self.storage[place_id] = tags

    def get_places_with_tag(self, tag: str) -> List[str]:
        return [place_id for place_id, tags in self.storage.items() if tag in tags]

    def top_tags(self, top_n: int) -> List[str]:
        tag_counts = Counter(tag for tags in self.storage.values() for tag in tags)
        sorted_tags = sorted(tag_counts.items(), key=lambda x: (-x[1], x[0]))
        return [tag for tag, _ in sorted_tags[:top_n]]


if __name__ == '__main__':
    pt = PlaceTagger()
    pt.add_place("p1", ["park", "green", "nature"])
    pt.add_place("p2", ["museum", "history"])
    pt.add_place("p3", ["park", "history"])
    pt.add_place("p4", ["museum", "art"])
    print(pt.storage)
    assert set(pt.get_places_with_tag("park")) == {"p1", "p3"}
    assert pt.top_tags(2) == ["history", "museum"]
