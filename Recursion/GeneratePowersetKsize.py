'''
Write a program which computes all size k subsets of 11,,2,...,?tl, where k and n are Pto- gram inputs. For example, iI k = 2 and n = 5, then the result is the following:
{{1, 2}, {1, 3}, {1, 4}, {1, 5}, [2, 3}, {2, 4}, {2, 5}, {3, 4}, {3, 5}, {4, 5}}
'''

'''
# Simple approach is first we check does it contain 1 or not.
# If not then first compute k size subset of [2...n] if contain 1 then we compute k-1 size subset of 2 to n and simply add 1 to each of them.
# Final answer will get if I take as an example 1,2,3 then {2,3},{1,3},{1,2}

Time Complexity: O(n*(2^k))
Space Complexity: O(n)
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        def directed_combine(nex,path):
            
            if len(path) == k:
                result.append(path)
                return 
            
            for i in range(nex,n+1):
                
                directed_combine(i+1,path+[i])
                
        directed_combine(1,[])
        return result
