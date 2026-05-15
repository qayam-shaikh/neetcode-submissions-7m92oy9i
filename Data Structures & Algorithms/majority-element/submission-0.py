class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maj = (float('-inf'), 0)
        for num, freq in count.items():
           maj = max((freq,num), maj) 
        return maj[1]
        
