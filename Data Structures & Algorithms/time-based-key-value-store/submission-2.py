class TimeMap:

    def __init__(self):
        # one key, different timestamp <-> values
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store.keys():
            self.store[key][timestamp] = value
        else:
            self.store[key] = {}
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store.keys():
            return ""
        if timestamp in self.store[key].keys():
            return self.store[key][timestamp]
        else:
            prev_max = -1
            for k in self.store[key].keys():
                if k < timestamp:
                    prev_max = max(prev_max,k)
            if prev_max == -1:
                return ""
            return self.store[key][prev_max]
        
