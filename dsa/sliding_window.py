# Fruit Into Baskets
# Write a function to calculate the maximum number of fruits you can collect from an integer array fruits, where each element represents a type of fruit. You can start collecting fruits from any position in the array, but you must stop once you encounter a third distinct type of fruit. The goal is to find the longest subarray where at most two different types of fruits are collected.
# Example:
# Input: fruits = [3, 3, 2, 1, 2, 1, 0]
# Output: 4
# Explanation: We can pick up 4 fruit from the subarray [2, 1, 2, 1]

def fruit_basket(fruits):
    start = 0
    window = {} # dict to store valid window
    max_fruit = 0

    for end in range(len(fruits)):
        window[fruits[end]] = window.get(fruits[end], 0) + 1

        # when window size exceed 2
        while len(window) > 2:
            window[fruits[start]] -= 1     # dec start - smaller window size
            if window[fruits[start]] == 0:  
             del window[fruits[start]]    # for valid window size
            start += 1

        max_fruit = max(max_fruit, end - start + 1)

    return max_fruit


# Longest Substring Without Repeating Characters
# Write a function to return the length of the longest substring in a provided string s where all characters in the substring are distinct.

# EXAMPLES
# Example 1: Input:s = "eghghhgg"

# Output:
# 3
# The longest substring without repeating characters is "egh" with length of 3.

def longest_substring(st):
    substring = {}
    max_length = 0
    start = 0

    for i in range(len(st)): # i = end
        substring[st[i]] = substring.get(st[i], 0) + 1
        print(substring, "-", substring[st[i]])
        while substring[st[i]] > 1:  # repeated char
           substring[st[start]] -= 1 # remove left side char
           start += 1                # move start pointer
        max_length = max(max_length, i - start + 1)
    return max_length

# Longest Repeating Character Replacement
# Write a function to find the length of the longest substring containing the same letter in a given string s, after performing at most k operations in which you can choose any character of the string and change it to any other uppercase English letter.

# EXAMPLES
# Input:
# s = "BBABCCDD"
# k = 2

# Output:
# 5
# Explanation: Replace the first 'A' and 'C' with 'B' to form "BBBBBCCDD". The longest substring with identical letters is "BBBBB", which has a length of 5.

def characterReplacement(s, k):
    state = {}
    max_freq = 0
    max_length = 0
    start = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) + 1
        max_freq = max(max_freq, state[s[end]])

        if k + max_freq < end - start + 1:  # for valid substring: k + max_freq >= window_length
            state[s[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)
    return max_length

# Maximum Sum of Subarray with Size K
# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
# Example:
# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.    

def max_sum_arr(nums, k):
    max_sum = 0
    start = 0
    state = 0

    for end in range(len(nums)):
        state += nums[end]

        if end - start + 1 == k:
            max_sum = max(max_sum, state)
            state -= nums[start]
            start += 1

    return max_sum


if __name__ == "__main__":
    print(longest_substring("eghghhgg"))