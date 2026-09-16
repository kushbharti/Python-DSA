class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        if len(s) % 2 != 0:
            return False

        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            else:    
                if len(stack) == 0:
                    return False
                
                last_item = stack.pop()
                if char != brackets[last_item]:
                    return False

                    
        
        return True if len(stack) == 0 else False