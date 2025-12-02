# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(s: str) -> bool:
        stack = []
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        for char in s:
            isClosingChar = char in closeToOpen
            if isClosingChar and stack and closeToOpen[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        isEmpty = len(stack) == 0
        return isEmpty


print(Solution.isValid("()[]{}"))
print(Solution.isValid("(}"))
