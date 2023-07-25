"""
Problem3  Rotate Array by K Places(https://leetcode.com/problems/rotate-array/)

"""

# Approach - 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        TC: O(nk) n = len(nums)
        SC = O(1)
        """
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

# Approach - 2

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        TC: O(n)
        SC: O(n)
        """
        
        if k == 0 or k==len(nums): return 
        n = len(nums)
        arr = [0 for i in range(n)]
        
        for i in range(n):
             arr[(i + k) % n] = nums[i]
           
            
        nums[:] = arr
