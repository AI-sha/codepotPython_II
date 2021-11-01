class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        # [Sentinel nodes serve as guardians and usually do not hold any data]

    def get(self, index: int) -> int:  # this function will return the node value at 'index'

        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head  # currently at sentinel node

        for _ in range(index + 1):  # take index+1 steps to reach the node at 'index'(starting from sentinel)
            curr = curr.next

        return curr.val  # return the value of the node required

    def addAtHead(self, val: int) -> None:

        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:

        # if index is greater than length, the node will not be inserted
        if index > self.size:
            return

        # if index is negative, the node will be inserted at the head of list
        if index < 0:
            index = 0

        self.size += 1  # as we are adding a node, we are increasing the size by one

        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)

        # node insertion
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return

        self.size -= 1  # as we are deleteing one node, we are reducing the size by one

        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)