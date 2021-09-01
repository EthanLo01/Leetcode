
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1431722/Python-easy-solution-using-hashMap
class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None:
            return 0

        if len(s) <= 1:
            return len(s)

        charMap = dict()
        start = 0
        longest = 0
        
        for i,c in enumerate(s):
            if c in charMap:
                start = max(start, charMap[c]+1)
            longest = max(longest, i-start+1)
            charMap[c] = i
        
        return longest