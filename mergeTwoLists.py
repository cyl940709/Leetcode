# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 将两个链表上的结点依次插入到新链表中，长的那一截链表最后全部赋值给新链表的next
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
    # 递归
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2
