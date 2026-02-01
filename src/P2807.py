import math
from typing import Optional, List
from UserDefinedDataType import ListNode

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        node1 = head
        node2 = head.next

        while node2:
            gcd_value = math.gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)

            node1.next = gcd_node
            gcd_node.next = node2

            node1 = node2
            node2 = node2.next

        return head
