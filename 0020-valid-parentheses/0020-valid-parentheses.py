class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            
            if bracket in "({[":
                stack.append(bracket)
            
            elif bracket in ")}]":
            
                if not stack:
                    return False
                
                if bracket == ')' and stack[-1] == '(':
                    stack.pop()
                elif bracket == ']' and stack[-1] == '[':
                    stack.pop()
                elif bracket == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0