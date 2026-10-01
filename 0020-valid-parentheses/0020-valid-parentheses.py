class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_open = {")":"(","}":"{","]":"["}

        if len(s) <= 1:
            return False
        
        for bracket in s:
            if bracket not in matching_open:
                stack.append(bracket)

            else:
                if not stack or stack[-1] != matching_open[bracket]:
                    return False
                stack.pop()
        
        return True if not stack else False
