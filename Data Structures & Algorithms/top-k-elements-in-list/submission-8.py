class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        res = []
        for i in range(n,-1,-1):
            j=0
            while k and j<len(buckets[i]):
                res.append(buckets[i][j])
                k-=1
                j+=1
            if k==0:
                return res

        
    