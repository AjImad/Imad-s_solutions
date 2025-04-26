# problem link: https://leetcode.com/problems/valid-parentheses

def isValid(s:str)->bool:

    mapping = {
        "(": ")",
        "{": "}",
        "[": "]",  
    }

    stack = [] # to tack opening

    for char in s:
        if char in mapping: # if True => char is opening
            stack.append[char] # push char to stack
        else: # char is not opening
            if not stack:
                return False # if char is not opening and stack empty => first char is closing
            top = stack.pop() # extract last opening from stack (Last in First Out)

            if char != mapping[top]: # if True => current char (closing) hasn't its opening
                return False
    
    return not stack