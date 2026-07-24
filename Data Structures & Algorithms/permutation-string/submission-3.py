class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counts1, counts2 = {}, {}

        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i],0)
            counts2[s2[i]] = 1 + counts2.get(s2[i],0)

        matches = 0
        for c in counts1:
            if counts1[c] == counts2.get(c, 0):
                matches += 1
        l = 0

        for r in range(len(s1),len(s2)):

            if matches == len(counts1):
                return True


            counts2[s2[r]] = 1 + counts2.get(s2[r],0) # add r
            if s2[r] in counts1:
                if counts1[s2[r]] == counts2[s2[r]]:
                    matches += 1
                elif counts1[s2[r]] + 1 == counts2[s2[r]]:
                    matches -= 1

            counts2[s2[l]] -= 1 # remove l
            if s2[l] in counts1:
                if counts1[s2[l]] == counts2[s2[l]]:
                    matches += 1
                elif counts1[s2[l]] - 1 == counts2[s2[l]]:
                    matches -= 1
             
            l += 1
        return matches == len(counts1)

            