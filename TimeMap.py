
#981. Time Based Key-Value Store
class TimeMap:
    def __init__(self):
        self.map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])
