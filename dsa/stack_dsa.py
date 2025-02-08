# Stack follows Last In, First Out (LIFO) principle
# which means that the last element added to 
# the stack is the first one to be removed

# basic: python array as stack
def arr_as_stack():
    arr_stack = []
    arr_stack.append(10)            # 10
    arr_stack.append(20)            # 10, 20
    arr_stack.pop()                 # 10
    arr_stack.append(30)            # 10, 30
    arr_stack.pop()                 # 10

# Valid Parentheses
# Given an input string s consisting solely of the characters '(', ')', ', ', '[' and ']', determine whether s is a valid string. A string is considered valid if every opening bracket is closed by a matching type of bracket and in the correct order, and every closing bracket has a corresponding opening bracket of the same type.

# Example
# Input: s = "(){({})}"
# Output: true

# Example
# Input: s = "(){({}})"
# Output: false

def valid_parenthesis(p):
    stack = []
    # map closing bracket to match starting stack bracket
    mapping = {")": "(", 
              "}": "{", 
              "]": "["}

    for c in p:
        if c in mapping:
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return True     # len(stack) == 0

# Decode String
# Given an encoded string, write a function to return its decoded string that follows a specific encoding rule: k[encoded_string], where the encoded_string within the brackets is repeated exactly k times. Note that k is always a positive integer. The input string is well-formed without any extra spaces, and square brackets are properly matched. Also, assume that the original data doesn't contain digits other than the ones that specify the number of times to repeat the following encoded_string.

# EXAMPLES
# Inputs:
# s = "3[a2[c]]"

# Output:
# "accaccacc"

def decode_string(s):
    stack = []
    currStr = ''
    currNum = 0

    for c in s:
        if c.isdigit():
            currNum = int(c)
        else:
            if c == '[':
                stack.append((currStr, currNum))
                currStr = ''
                currNum = 0
            elif c == ']':
                prevStr, num = stack.pop()
                currStr = prevStr + num * currStr
            else:
                currStr += c
    return currStr


# Largest Rectangle in Histogram
# Given an integer array heights representing the heights of histogram bars, write a function to find the largest rectangular area possible in a histogram, where each bar's width is 1.

# EXAMPLES
# Inputs:
# heights = [2,8,5,6,2,3]

# Output:
# 15

def largest_rect(heights):
    n = len(heights)
    stack = []
    max_area = 0
    
    for i in range(n):
        # current element is smaller than the top of the stack
        while stack and heights[stack[-1]] >= heights[i]:
            # smallest element of the histogram
            tp = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[tp] * width)        
        stack.append(i)
    
    # remaining items in the stack, next smaller does not exist
    # previous smaller is the item just below in the stack
    while stack:
        tp = stack.pop()
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, heights[tp] * width)
    
    return max_area

if __name__ == "__main__":
    # print(valid_parenthesis("(){({})}"))
    # print(decode_string("2[a4[c]]"))
    print(largest_rect([2,8,5,6,7,2,3]))