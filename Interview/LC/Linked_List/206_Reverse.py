class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        current = head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        head = prev

        return head