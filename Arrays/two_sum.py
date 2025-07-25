# Problem: https://leetcode.com/problems/two-sum/
# Approach: Hash Map
# Date: July 10, 2025

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []  


feat: solved 'Two Sum' using hash map approach!
