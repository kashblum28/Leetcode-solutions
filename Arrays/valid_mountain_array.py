# Problem: https://leetcode.com/problems/valid-mountain-array/
# Approach: climb up and then down...using two pointers
# Difficulty: Easy
# Date: July 12, 2025

class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False  
        
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False 
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1


feat: solved 'Valid Mountain Array' using two-pointer climb

