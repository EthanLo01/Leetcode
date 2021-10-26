# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:45:40 2021

@author: user
"""
# original
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ans = []
        for rn in range(rowIndex+1):
            row = [ None for _ in range(rn+1)]
            row[0] = 1
            row[-1]= 1


            for j in range(1, len(row) -1):
                row[j] = ans[rn -1][j -1]+ ans[rn - 1][j]

            ans.append(row)



        return row