"""
Problem link: https://leetcode.com/problems/search-insert-position/
description:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

def searchInsert(nums, target):
    # binary search: is a highly efficient search method used to find a specified value withing a sorted list or array, it work by repeatedly divide the search interval on half until the target is found or interval is empty 
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    # if not found, left is the position to insert
    return left

    #another way:
    # previews = nums[0]

    # if target not in nums:
    #     for i, v in enumerate(nums):
    #         if target > previews and target < v:
    #             return i
            
    #         previews = v

    #         if v == nums[len(nums)-1] and target > v:
    #             return i+1
            
    #     return 0
    
    # for i, n in enumerate(nums):
    #     if target == n:
    #         return i