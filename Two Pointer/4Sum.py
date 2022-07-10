class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        foursum = []
        
        for i in range(n-3):
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                self.threesum(i,j,target,nums,foursum)
                
        return foursum
                
    def threesum(self,first,second,target,nums,foursum):
        
        l = second+1
        r = len(nums) - 1
        
        while l < r:
            
            sum = nums[first] + nums[second] + nums[l] + nums[r]
            
            if sum == target:
                foursum.append([nums[first],nums[second],nums[l],nums[r]])
                l+=1
                
                while nums[l] == nums[l-1] and l < r:
                    l+=1
                    
            elif sum < target:
                l+=1
            
            else:
                r-=1
