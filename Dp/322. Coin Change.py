# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 20:22:44 2021

@author: user
"""

# https://leetcode.com/problems/coin-change/discuss/1512989/Python-Dynamic-Programming-tabulation-Faster-than-91-solutions 
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[-1]*(amount+1)
        dp[0]=0
        for coin in coins:
            for x in range(amount+1):
                if dp[x]!=-1 and x+coin<=amount:
                    if dp[x+coin]==-1: dp[x+coin]=dp[x]+1
                    else: dp[x+coin]= min(dp[x+coin],dp[x]+1)
        print( dp[-1])


# Solution
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
      
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
        
        