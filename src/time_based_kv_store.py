from typing import List, Dict


class TimeMap:
    def __init__(self):
        self.db: Dict[str, List[str, int]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
        self.db[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values: List[str, int] = self.db.get(key, [])

        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2

            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res
