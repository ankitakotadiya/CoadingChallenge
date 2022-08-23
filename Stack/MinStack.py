'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
'''

'''
# Here we need to design a stack that perform stacks basic operation such as Push, Pop, Min and Top.

# Push - Append new element at top of the stack. Also if value less than the current minimum value then store curmin value to the prevmin and current value to the curmin.
# Pop - Pop element from the stack, if stack is not empty. If value is equal to curmin then pop value from the prevmin and save it to the curmin
# Top - Get last inserted from the stack.
# Min - Return curmin that we have stored.

Time Complexity: O(1)
Space Complexity: O(n)
'''

class MinStack:

    def __init__(self):
        
        self.stack = []
        self.prevmin = []
        self.curmin = float('inf')

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        
        if val <= self.curmin:
            self.prevmin.append(self.curmin)
            self.curmin = val
        
    def pop(self) -> None:
        
        if self.stack[-1] == self.curmin:
            self.curmin = self.prevmin.pop()
            
        self.stack.pop()
            
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.curmin
