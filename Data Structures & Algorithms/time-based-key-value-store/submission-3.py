class TimeMap:

    def __init__(self):
        self.mymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mymap.keys():
            self.mymap[key].append([timestamp, value])
        else:
            self.mymap[key] = [[timestamp,value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mymap.keys():
            pairs = self.mymap[key]
        else:
            return ''
        l = 0
        r = len(pairs)-1
        print(pairs)
        while(l <= r):
            mid = (l + r) // 2
            print(l,r,mid)
            if pairs[mid][0] < timestamp:
                l = mid + 1
            elif pairs[mid][0] > timestamp:
                r = mid - 1
            else:
                return pairs[mid][1]
        if pairs[l-1][0] <= timestamp:
            return pairs[l-1][1]
        return ""
