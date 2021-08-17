# original:
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        try:
            if nums[0] == nums[1] == nums[2]:

                index = 0
                count = 0

                for i in range(1, len(nums)):
                    # if(nums[i-1]==nums[i]):
                    #     nums[index] = nums[i]
                    #     count += 1

                    if nums[i-1] != nums[i]:
                        count = 0

                    if count < 2:
                        nums[index] = nums[i]
                        index+=1
                        count+=1

            else:

                index = 1
                count = 0

                for i in range(1, len(nums)):
                # if(nums[i-1]==nums[i]):
                #     nums[index] = nums[i]
                #     count += 1

                    if nums[i-1] != nums[i]:
                        count = 0

                    if count < 2:
                        nums[index] = nums[i]
                        index+=1
                        count+=1

        except:
            index = 1
            count = 0

            for i in range(1, len(nums)):
            # if(nums[i-1]==nums[i]):
            #     nums[index] = nums[i]
            #     count += 1

                if nums[i-1] != nums[i]:
                    count = 0

                if count < 2:
                    nums[index] = nums[i]
                    index+=1
                    count+=1

        return index
    
#God
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            each = nums[i]
            if nums.count(each) > 2:
                nums.remove(each)
                i -= 1

            i += 1
        return len(nums)