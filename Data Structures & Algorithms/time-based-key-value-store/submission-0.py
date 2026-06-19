class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr=self.hashmap[key]
        n=len(arr)
        if n==0: return ""
        l,r=0,n-1
        ans=-1
        while l<=r:
            m=(l+r)//2
            if timestamp>=arr[m][0]:
                ans=m
                l=m+1
            else:
                r=m-1
        if ans==-1: return ""
        return arr[ans][1]
            
