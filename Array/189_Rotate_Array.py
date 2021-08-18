# original:
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        new_nums = [0] * len(nums)
        for i in range(len(nums)):

            index = i+k
            while index >= len(nums):
                index = index - len(nums)


            new_nums[index] = nums[i] #新的值
        # nums = [i for i in new_nums]
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
 
    
    
#God
class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k!=0: nums[:] = nums[-k : ] + nums[ :len(nums)-k]