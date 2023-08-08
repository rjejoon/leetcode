from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        lo, hi = 0, len(self.dict[key])-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if timestamp == self.dict[key][mid][0]:
                return self.dict[key][mid][1]
            elif timestamp < self.dict[key][mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        return '' if lo-1 < 0 else self.dict[key][lo-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == '__main__':
    tm = TimeMap()
    tm.set('love', 'high', 10)
    tm.set('love', 'low', 20)
    print(tm.dict)
    print(tm.get('love', 5))
    print(tm.get('love', 10))
    print(tm.get('love', 15))
    print(tm.get('love', 20))
    print(tm.get('love', 25))
