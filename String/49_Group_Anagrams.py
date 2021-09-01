# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:44:58 2021

@author: user
"""

# https://leetcode.com/problems/group-anagrams/discuss/1421025/Python-Simple-Faster-and-Easy-to-understand
class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:                   #iterating through the list strs to obtain each word
            ordered = ''.join(sorted(word)) #sorting each letter in the word and joining the letters
            if ordered not in d:            #if the sorted word intance is not present in the dictionary, add it and let the value be the word (which is unsorted)
                d[ordered] = [word]
            else:                           #else add the word to the value which is a list
                d[ordered] += [word]
        return d.values()                   #finally return the dictionary values