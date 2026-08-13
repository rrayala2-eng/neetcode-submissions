class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i : j + 1])  # ✅ correct list name
                    dfs(j + 1)
                    part.pop()

        dfs(0)       # ✅ called once, at partition's level, after dfs is defined
        return res   # ✅ returned from partition, not from inside dfs

    def isPalin(self, s, l, r):  # ✅ name matches the call site
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True