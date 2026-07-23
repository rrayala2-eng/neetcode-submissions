class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        v = {}
        i = 0
        res = 0

        for j in range(len(s)):
            if s[j] in v:
                i = max(v[s[j]],i)
            res = max(res,j - i + 1)
            v[s[j]] = j+ 1
        return res
        