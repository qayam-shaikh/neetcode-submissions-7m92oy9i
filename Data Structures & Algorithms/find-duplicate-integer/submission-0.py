class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                return arr[i]