class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        
        for left in range(len(haystack) - nlen + 1):
            right = left + nlen

            if haystack[left:right] == needle:
                return left
        return -1