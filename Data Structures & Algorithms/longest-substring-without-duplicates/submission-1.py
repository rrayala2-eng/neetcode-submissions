class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        v = {}
        i = 0
        ans = 0

        for j in range(len(s)):
            if s[j] in v:
                i = max(i,v[s[j]])
            v[s[j]] = j + 1
            ans = max(ans,j - i + 1)
        return ans
