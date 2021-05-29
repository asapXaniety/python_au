# Design

+[Min Stack](#min-stack)

## Min Stack

https://leetcode.com/problems/min-stack/

```python
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        self.stack.append(val)
        

    def pop(self):
        self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return min(self.stack)
```