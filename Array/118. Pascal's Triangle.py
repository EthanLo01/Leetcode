# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 07:55:58 2021

@author: user
"""
# original
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        if numRows> 2:
            ans = [[1],[1,1]]
            last = [1,1]
            for i in range(numRows-2):
                temp = [1]
                for i in range(len(last)-1):
                    temp.append(last[i] + last[i+1])

                temp.append(1)

                last = temp

                ans.append(temp)


        return ans
            
#https://leetcode.com/problems/pascals-triangle/discuss/1451090/Python-or-DP
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for rn in range(numRows):
            row = [ None for _ in range(rn+1)]
            row[0] = 1
            row[-1]= 1


            for j in range(1, len(row) -1):
                row[j] = ans[rn -1][j -1]+ ans[rn - 1][j]

            ans.append(row)



        return ans
            
            
