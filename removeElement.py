"""
Problem link: https://leetcode.com/problems/remove-element
"""

def removeElement(nums, val):
    pointer = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[pointer] = nums[i]
            pointer += 1

    return pointer