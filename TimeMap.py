
#981. Time Based Key-Value Store
class TimeMap:
    def __init__(self):
        self.map = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

if __name__ == "__main__":
    ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    args = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    out = []
    obj = None
    for op, a in zip(ops, args):
        if op == "TimeMap":
            obj = TimeMap()
            out.append(None)
        elif op == "set":
            obj.set(a[0], a[1], a[2])
            out.append(None)
