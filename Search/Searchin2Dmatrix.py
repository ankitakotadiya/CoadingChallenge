'''
# The approach is binary search.
# Run the loop number of rows time and consider each row as a single array and perform binary search on it.
# Binary search steps as followed:
  - Set left and right pointer at 0 and last index and find out mid point.
  - if mid point is equal to the target element then return True we have found and break the loop.
  - If mid is greater than the target then discard right part our element is placed somewhere in the left part.
  - If mid is less than the target element then discard left part.
  - If not found then return False.
  
# Keep travesing each rows until binary search returns result False.

Time Complexity: O(nLogn), where n is the number of rows.
Space Complexity: O(1)
'''

'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(arr):
            
            l = 0
            r = len(arr) - 1
            
            while l <= r:
                
                mid = (l+r)//2
                
                if arr[mid] == target:
                    return True
                
                elif arr[mid] < target:
                    l = mid+1
                    
                else:
                    r = mid-1
                    
            return False
        
        n = len(matrix)
        result = False
        y = 0
        while result == False and y < n:
            
            result = binary_search(matrix[y])
            y+=1
            
        return result
