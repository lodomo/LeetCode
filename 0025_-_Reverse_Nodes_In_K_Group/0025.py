from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        if k == 2:
            return self.swapPairs(head)

        return self.reverse_list(head, k)

    def reverse_list(self, head, k):
        if not head:
            return head

        current = head
        count = 0
        while current and count < k:
            current = current.next
            count += 1

        if count == k:
            current = self.reverse_list(current, k)
            while count > 0:
                temp = head.next
                head.next = current
                current = head
                head = temp
                count -= 1
            head = current
        return head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        third = head.next.next
        first = head.next
        second = head

        first.next = second
        second.next = self.swapPairs(third)
        return first


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 5

answer = Solution().reverseKGroup(head, k)
while answer:
    print(answer.val)
    answer = answer.next
