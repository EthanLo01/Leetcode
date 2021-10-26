# original Time Limit Exceeded
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        nums.sort()
        for i  in range(len(nums)):

            if i == len(nums)-1:
                return ans



            first = nums[i]
            j = i+1
            for j in range(i+1, len(nums)):

                sec = nums[j]

                l = j+1
                
                cheak = 0-(first+sec)
                
                # if max(nums[j:]) + cheak< 0:
                #     continue
                    
                if cheak in nums[j+1:]:
                    third = cheak
                    temp = [first, sec, third]
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)

        return ans
    
# https://leetcode.com/problems/3sum/discuss/1404526/Easy-to-understand-Python-solution-or-Three-pointers
class Solution:
    def threeSum(self, nums):
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            h = len(nums)-1
            while l<h:
                if (nums[i]+nums[l]+nums[h])==0:
                    res.add((nums[i], nums[l], nums[h]))
                    l += 1
                    while nums[l]==nums[l-1] and l<h:
                        l += 1
                elif (nums[i]+nums[l]+nums[h])<0:
                    l += 1
                else:
                    h -= 1
        return res