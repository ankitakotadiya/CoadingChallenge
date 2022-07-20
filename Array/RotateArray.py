class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        l = 0
        
        while l < k:
            
            lastval = nums.pop(-1)
            nums.insert(0,lastval)
            l+=1
