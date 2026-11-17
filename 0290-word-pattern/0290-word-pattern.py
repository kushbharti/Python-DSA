class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        match_dict = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in match_dict:
                if match_dict[ch] != word:
                    return False
            else:
                if word in match_dict.values():
                    return False
                match_dict[ch] = word
        return True