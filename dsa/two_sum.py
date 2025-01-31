# Two Sum
# Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
# Example:
# Input: nums = [1,3,4,6,8,10,13], target = 13
# Output: True (3 + 10 = 13)
# Input: nums = [1,3,4,6,8,10,13], target = 6
# Output: False

def pair_sum(num, target):              # O(n^2)
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return True
            return False
        

def two_sum(nums, target):              # O(n)
    left, right = 0, len(nums) - 1
      
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return True

        if current_sum < target:
            # all other pairs in left pointer also have sums less than target
            left += 1
        else:
            right -= 1
      
    return False        

# Container With Most Water
# Given an integer input array heights representing the heights of vertical lines, write a function that returns the maximum area of water that can be contained by two of the lines (and the x-axis). The function should take in an array of integers and return an integer.
# Inputs:
# heights = [3,4,1,2,2,4,1,3,2]

# Output:
# 21

def max_area(heights):
    left, right = 0, len(heights) - 1
    current_max = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height

        current_max = max(current_max, current_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return current_max


# 3-Sum
# Given an input integer array nums, write a function to find all unique triplets [nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, and the sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting list does not contain any duplicate triplets.
# Input:
# nums = [-1,0,1,2,-1,-1]

# Output:
# [[-1,-1,2],[-1,0,1]]

def three_sum(nums):                    # O(n^2)
    nums.sort()
    result = []
    # i reaches the 2nd to last element in the array 
    # because we need at least 3 elements to form a triplet
    for i in range(len(nums) - 2):    
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            # calculate sum of triplets
            total = nums[i] + nums[left] + nums[right] 
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # append triplets (when their sum is 0)
                result.append([nums[i], nums[left], nums[right]])
                # if left and successor number same
                # move left pointer to avoid duplicate
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # move right backwards
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


# Triangle Numbers
# Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle. The triplets do not need to be unique.
# EXAMPLES
# Input:
# nums = [11,4,9,6,15,18]

# Output:
# 10

def tri_number(nums):
    # In order for a triplet to be valid lengths of a triangle
    # the sum of any two sides must be greater than the third side
    nums.sort()
    count = 0
    for i in range(len(nums)-1, 1, -1):  # backward
        left = 0
        right = i-1
        while left < right:
            if nums[left] + nums[right] >= nums[i]:
                # as we sorted nums, i is largest
                # so left and right are smaller than i
                # left < right < i
                # sum(l+r) > i
                count += right - left
                right -= 1
            else:
                # sum is smaller - invalid triplets
                left += 1
        return count

# Move Zeroes
# Given an integer array nums, write a function to rearrange the array by moving all zeros to the end while keeping the order of non-zero elements unchanged. Perform this operation in-place without creating a copy of the array.

# EXAMPLES
# Input:
# nums = [2,0,4,0,9]

# Output:
# [2,4,9,0,0]

def move_zero(nums):
    check_num = 0 # init with zero
    for i in range(len(nums)): # init i with 0
        if nums[i] != 0:
            # swap
            nums[check_num], nums[i] = nums[i], nums[check_num]
            check_num += 1


# Sort Colors
# Write a function to sort a given integer array nums in-place (and without the built-in sort function), where the array contains n integers that are either 0, 1, and 2 and represent the colors red, white, and blue. Arrange the objects so that same-colored ones are adjacent, in the order of red, white, and blue (0, 1, 2).

# EXAMPLES
# Input:
# nums = [2,1,2,0,1,0,1,0,1]

# Output:
# [0,0,0,1,1,1,1,2,2]

def sort_color(nums):
    left, right = 0, len(nums)-1
    i = 0

    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
    return nums



if __name__ == "__main__":
    res = three_sum([-1,0,1,2,-1,-1])
    print(res)