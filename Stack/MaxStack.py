'''
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
'''

'''
# Here we need to design a stack that perform stacks basic operation such as Push, Pop, Peekmax and Top.
# Push - Append new element at top of the stack. Also if value greater than the curmax value then store curmax value to the prevmax and current value to the curmax.
# Pop - Pop element from the stack, if stack is not empty. If value is equal to curmax then pop value from the prevmax and save it to the curmax
# Top - Get last inserted from the stack.
# Peekmax - Return curmax that we have stored.
# PopMax - If last value in prevmax equal to the curmax then first will pop prevmax. Now will remove curmax from the stack and store curmax equal to the last element of prevmax.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class MaxStack:

    def __init__(self):
        
        self.stack = []
        self.prevmax = []
        self.curmax = float('-inf')

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        
        if val >= self.curmax:
            self.prevmax.append(self.curmax)
            self.curmax = val
        
    def pop(self) -> None:
        
        if self.stack[-1] == self.curmax:
            self.curmax = self.prevmax.pop()
            
        self.stack.pop()
            
    def top(self) -> int:
        return self.stack[-1]
        

    def peekmax(self) -> int:
        return self.curmax
      
    def popMax(self):
      
      if self.prevmax[-1] == self.curmax:
        self.prevmax.pop()
        
      indx = self.stack.index(self.curmax)
      self.stack.pop(indx)
      self.curmax = self.prevmax[-1]
