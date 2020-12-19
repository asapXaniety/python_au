# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle Of The Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

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

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tail = start = ListNode(0)
        while l1 != None and l2 != None: 
            if l1.val < l2.val:
                tail.next = l1 
                l1 = l1.next 
            else: 
                tail.next = l2
                l2 = l2.next
            tail = tail.next 
        if l1 is None:
            tail.next = l2
        if l2 is None:
            tail.next = l1
        return start.next
```

## Remove nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        amount = 0
        while curr is not None:
            curr = curr.next
            amount = amount + 1
        k = amount - n #Поиск номера нужного элемента
        prev = None
        nxt = head
        while k!= 0:
            prev = nxt
            nxt = nxt.next
            k = k - 1
        if prev is None:
            return head.next
        else:
            prev.next = nxt.next
            nxt.next = None
        return head
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        bol = False
        first = second = head
        while (second is not None and second.next is not None):
            first = first.next
            second = second.next.next
            if (first == second):
                bol = True
                break
        if bol is False:
            return None
        second = head
        while (first != second):
            first = first.next
            second = second.next
        return first
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        bol = False
        first = second = head
        while (second is not None and second.next is not None):
            first = first.next
            second = second.next.next
            if (first == second):
                bol = True
                break
        return bol
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = 0
        len_B = 0 
        A = headA
        B = headB
        while (A is not None):
            A = A.next
            len_A = len_A + 1
        while (B is not None):
            B = B.next
            len_B = len_B + 1
        if (len_A < len_B):
            while (len_A != len_B):
                headB = headB.next
                len_B = len_B - 1
        if (len_B < len_A):
            while (len_A != len_B):
                headA = headA.next
                len_A = len_A - 1
        while (headA is not None or headB is not None):
            if (headA == headB):
                return headA
            else:
                headA = headA.next
                headB = headB.next
```
