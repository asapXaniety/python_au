#Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle Of The Linked List](#middle-of-the-linked-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list

```python
# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while (current != None):
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous
```


## Middle Of The Linked List

https://leetcode.com/problems/middle-of-the-linked-list

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        a = []
        while current is not None:
            a.append(current)
            current = current.next
        return a[len(a)//2]
```




