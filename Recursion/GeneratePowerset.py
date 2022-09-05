'''
The power set of a set S is the set of all subsets of S, includingboth the empty set 0 and S itself.
Write a function that takes as input a set and retums its power set.

Thesetofsubsetsof {0,1,2}thenis Ul,{21,{1,),{1.,2]111union with {{0}, {0,2]1,{0,1},{0,1.,2]r]1,i.e., {{}, l2l,[1],{1,2],{Ol,{O,Zl,{0,U,{0,1.,2]1,
'''

'''
# First we select first element and compute subset of next to last element then will select next element and compute subset next to last will follow the process until reach to last element.
# Once we see last element append subset to result list and we just do union of last to previous subset and append to our result one by one.

# Let's say I have set {0,1,2} so first pick an element 0 and compute subset of {1,2}. To do this, will select 1 that leaves us {2}. Now we pick 2 so the subset of 2 is union with {} and {2} that is {{}.{2}}.
# Subset of {1,2} is union with {{},{2}} and {{1},{1,2}} that is {{},{1},{2},{1,2}}. Subset of {0,1,2} is now union with previous and subset of {0,1,2} would get an answer.

Time Complexity: O(n*2^n)
Space Compexity: O(n)
'''

def generate_power_set(input_set):
  
  def directed_power_set(to_be_selected,selected_so_far):
    
    if to_be_selected == len(input_set):
      power_set.append(list(selected_so_far))
      return
    
    directed_power_set(to_be_selected+1,selected_so_far)
    directed_power_set(to_be_selected+1,selected_so_far + [input_set[to_be_selected]])
    
  power_set = []
  directed_power_set(0,[])
  
  
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(num,path,res=[]):
            
            res.append(path)
            
            for i in range(len(num)):
                
                dfs(num[i+1:],path+[num[i]])
                
            return res
        
        return dfs(nums,[])
    
    

