# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        tmp=[]
        while pHead:
            if pHead in tmp:
                return pHead
            else:
                tmp.append(pHead)
            pHead=pHead.next
