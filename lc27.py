# Remove Element
# Given an integer array nums and an integer val,remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k get get accepted, you need to do the following things:
# 1.Chnage the array nums such that the first k elements of nums contain the elements which are not equal to val.The remaining elements of nums are not important as well as the size of nums
# 2.Return k

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. count the number of elements which are not equal to val
        # 2. change the array nums such that the first k elements of nums contain the elements which are not equal to val
        # 3. return k
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        return count
