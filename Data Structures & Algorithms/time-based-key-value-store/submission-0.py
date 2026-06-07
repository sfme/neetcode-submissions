class TimeMap:

    def __init__(self):

        self.hash_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.hash_map:
            self.hash_map[key].append((value, timestamp))

        else:
            self.hash_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:

        if key in self.hash_map:

            l = 0
            r = len(self.hash_map[key]) - 1

            res = ""

            while l <= r:

                mid = l + (r - l) // 2

                if self.hash_map[key][mid][1] <= timestamp:
                    res = self.hash_map[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1

            return res
            
        else:
            return ""
        