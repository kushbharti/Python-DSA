class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        counter = 0
        max_len = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[counter])
                counter += 1
            seen.add(s[i])

            current_len = i - counter + 1
            max_len = max(max_len, current_len)
        
        return max_len