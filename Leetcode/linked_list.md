# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle Of The Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)

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

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        current = head
        while(current):
            lst.append(current.val)
            current = current.next
        p1 = 0
        p2 = len(lst)-1
        while(p1<p2):
            if lst[p1]!=lst[p2]:
                return False
            else:
                p1+=1
                p2-=1
        return True
```
