# Problem: https://leetcode.com/problems/move-zeroes/
# Approach: Two_pointer
# Difficulty: Easy
# Date: July 12, 2025

class Solution:
    def moveZeroes(self, nums):
        write_index = 0
        
        for read_index in range(len(nums)):
            if nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        for i in range(write_index, len(nums)):
            nums[i] = 0

feat: solved 'Move Zeroes' using two-pointer swap
