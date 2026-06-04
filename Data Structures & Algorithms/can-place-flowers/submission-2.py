class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(fb)):
            if fb[i]==0 and (i==0 or fb[i-1]==0) and (i==len(fb)-1 or fb[i+1]==0):
                fb[i]=1
                cnt+=1
            if cnt>=n:
                return True
        return cnt>=n