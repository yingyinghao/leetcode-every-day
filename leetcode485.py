# Given a binary array nums, return the maximum number of
# consecutive 1's in the array

class Solution:
    def findMaxConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
