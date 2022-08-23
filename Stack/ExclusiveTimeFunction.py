'''
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
'''

'''
# Here will use stack to the track of three things such as ID, (start | end) action and (start | end) time.
# Will use one result array which length is equal to n and intially set all elements as 0.
# Run through loop of number of logs.
# Each and every iteration get ID, action and time and check if action = 'start' then simply store ID and Time at the top of the stack.
# When you reach to the end action so you need to pop last element from the which contains ID and start time.
# To calculate number of unit will substract start time from end and update result array element at ID index.
# After performing this calculation, still any element remains in stack then get ID and update result array element at that particular ID and substract current unit from it.
# So next time for the same ID we can easily remove unit which was not travelled by that ID.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        stack = []
        cnt = [0]*n
        
        for log in logs:
            
            ID,action,time = log.split(':')
            ID = int(ID)
            time = int(time)
            
            if action == 'start':
                stack.append([ID,time])
                
            elif action == 'end':
                _,strt = stack.pop()
                add = time+1-strt
                cnt[ID] += add
                
                if stack:
                    cnt[stack[-1][0]] -= add
                    
        return cnt
