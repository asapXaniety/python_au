class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        self.count = 0

        def get(self, index: int) -> int:
            """
            Get the value of the index-th node in the linked list. If the index is invalid, return -1.
            """
            if index < 0 or index >= self.size:
                return -1

            current = self.head
            for i in range(0, index):
                current = current.next

            return current.val

        def addAtHead(self, val: int) -> None:
            """
            Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
            """
            self.addAtIndex(0, val)

        def addAtTail(self, val: int) -> None:
            """
            Append a node of value val to the last element of the linked list.
            """
            self.addAtIndex(self.size, val)

        def addAtIndex(self, index: int, val: int) -> None:
            """
            Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
            """
            if index > self.size:
                return

            current = self.head
            NewNode = ListNode(val)

            if index <= 0:
                NewNode.next = current
                self.head = NewNode
            else:
                for i in range(index-1):
                    current = current.next
                NewNode.next = current.next
                current.next = NewNode

            self.size += 1

        def deleteAtIndex(self, index: int) -> None:
            """
            Delete the index-th node in the linked list, if the index is valid.
            """
            if index < 0 or index >= self.size:
                return

            current = self.head

            if index == 0:
                self.head = self.head.next
            else:
                for i in range(0, index-1):
                    current = current.next
                current.next = current.next.next

            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

        def Print_Linked_List(self):
            x = self.head
            for i in range(self.size):
                print(x.val)
                x = x.next

        def __next__(self):
            if self.count < self.size:
                self.count += 1
                return self.get(self.count - 1)
            else:
                raise StopIteration

        def __iter__(self):
            return self