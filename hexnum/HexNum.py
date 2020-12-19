import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, num):
        x = Node(num[0])
        self.head = x
        self.size = len(num)
        for i in range(1, len(num)):
            x.next = Node(num[i])
            x = x.next

    def transform(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        x = self.head
        for i in range(self.size):
            if x.val in letters:
                x.val = 10 + letters.index(x.val)
            else:
                x.val = int(x.val)
            x = x.next
        return self

    def retransform(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        x = self.head
        for i in range(self.size):
            if x.val > 9:
                x.val = letters[x.val - 10]
            x = x.next
        return self

    def multiply(self, second):
        self = self.transform()
        second = second.transform()
        if self.size < second.size:
            first = second
            second = self
        else:
            first = self
        size = second.size
        x = first
        first = first.head
        second = second.head
        for i in range(size):
            if first.val + second.val <= 15:
                first.val = first.val + second.val
            else:
                sum = first.val + second.val
                sum -= 16
                if i is (x.size - 1):
                    point = Node(0)
                    first.next = point
                    x.size += 1
                first.next.val += 1
                if first.next.val >= 16:
                    y = first.next
                    while y.val >= 16:
                        y.val -= 16
                        if y.next is None:
                            y.next = Node(0)
                            x.size += 1
                        y.next.val += 1
                        y = y.next
                first.val = sum
            first = first.next
            second = second.next
        x = x.retrasform()
        return x

    def __str__(self):
        result = ""
        x = self.head
        for i in range(self.size):
            x.val = str(x.val)
            result = result + x.val
            x = x.next
        result = result[::-1]
        return result


def main(first, second):
    second = second[::-1]
    first = first[:: -1]
    first = LinkedList(first)
    second = LinkedList(second)
    first = first.multiply(second)
    print(first)


if __name__ == '__main__':
    hexnum = sys.argv
    main(hexnum[1], hexnum[2])