# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative
# order of the non-zero elements.
# NOTE you must do this in-place without making a copy of the array

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 1. count the number of zeros
        # 2. move all the non-zero elements to the front
        # 3. fill the remaining elements with zeros
        # 4. return the modified array
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1

        return nums
