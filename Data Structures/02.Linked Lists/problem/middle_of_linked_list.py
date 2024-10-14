# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        node1 = head
        node2 = head

        while node2 and node2.next:

            node1 = node1.next
            node2 = node2.next.next

        return node1