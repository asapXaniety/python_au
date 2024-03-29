# Design

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)

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

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
class MyQueue:

    def __init__(self):
        self.item = []

    def push(self, x):
        self.item.insert(0, x)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def empty(self):
        return not self.item
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
class MyStack:

    def __init__(self):
        self.queue = []


    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop()


    def top(self):
        return self.queue[-1]

    def empty(self):
        return self.queue == []
```