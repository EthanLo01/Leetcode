# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 01:45:31 2021

@author: user

"""
# https://ithelp.ithome.com.tw/articles/10218585
# God:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        result = 0;
        pre = 1;
        next = 2;
        i = 3
        while i <= n:


            result = pre + next
            pre = next
            next = result
            i +=1
            

        return result;