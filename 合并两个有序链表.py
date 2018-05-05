"""

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

"""
解题思路：

对于链表操作，需要注意指针的使用，用两个指针遍历这两个链表，将当前两个指针的较小的一个内容接在返回链表的最后，
再将该较小指针后移一位，直到其中一个指针的内容为空，则结束。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next

if __name__ == '__main__':
    x1 = [1, 2, 4]
    x2 = [1, 3, 4]
    b = Solution()
    print(b.mergeTwoLists(l1=x1, l2=x2))
