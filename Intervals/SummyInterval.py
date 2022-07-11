class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        def help_foo(arr,left,right):
            
            if abs(left-right)>=1:
                return f'{arr[left]}->{arr[right]}'
            
            return f'{arr[left]}'
        
        res=[]
        left = 0
        
        if len(nums) == 1:
            return list(map(str,nums))
        
        for i in range(1,len(nums)):
            
            if abs(nums[i] - nums[i-1]) > 1:
                res.append(help_foo(nums,left,i-1))
                left = i
                
            if i == len(nums) - 1:
                res.append(help_foo(nums,left,i))
        
        return res
