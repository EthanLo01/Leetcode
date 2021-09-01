# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:54:05 2021

@author: user
"""

# https://leetcode.com/problems/reverse-linked-list/discuss/1422245/python-while-loop
class Solution(object):
    def reverseList(self, head):

        output = None
        while head != None:
            temp = ListNode(head.val, output)
            output = temp
            head = head.next
        return output