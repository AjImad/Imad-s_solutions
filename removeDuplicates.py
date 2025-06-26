"""
Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

def removeDuplicates(nums):
    if not nums:
        return 0 # if nums is empty => 0 unique elements
    
    insert_pos = 1 # equal to 1 because first element (0) is always unique, it's a marker to know where to write the next unique element

    #loop over nums starting from 1, index 0 has no previews element to compare with
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]: # if true => current element is a unique element
            nums[insert_pos] =  nums[i] # modify nums in-place
            insert_pos += 1 # increment insert pos to prepare for the next unique element and also count the unique elements

    return insert_pos
