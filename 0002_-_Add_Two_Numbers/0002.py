# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        nodes = ListNode(l1.val + l2.val)
        cur = nodes

        if cur.val >= 10:
            cur.val -= 10
            remainder = 1

        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            val = l1.val + l2.val + remainder
            remainder = val // 10
            val %= 10
            cur.next = ListNode(val)
            cur = cur.next

        if remainder:
            cur.next = ListNode(remainder)

        return nodes
