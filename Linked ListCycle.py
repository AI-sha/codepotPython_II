# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

'''  using Hashmap time limit exceeded
class LinkedListCycle:
    def hasCycle(self, head: ListNode) -> bool:

        nodes_seen = set()  # create a set to store all values of nodes
        while head is not None:  # if head is none, then it means we reached end and linked list is non cyclic
            if head is nodes_seen:  # if we reach any node that was already seen - means cyclic
                return True
            nodes_seen.add(head)  # if node not seen already, add it in the set
            head = head.next  # move to next node
        return False  # when we reach end of list
'''

# Using Floyd's cycle finding Algo:

class LinkedListCycle:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True  # if slow = fast, it means cyclic

''' 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Input: head = [3,2,0,-4], pos = 1
Output: true
'''