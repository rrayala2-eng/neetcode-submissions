class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counts1, counts2 = {}, {}

        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
            counts2[s2[i]] = 1 + counts2.get(s2[i], 0)

        matches = 0
        for c in counts1:
            if counts1[c] == counts2.get(c, 0):
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(counts1):
                return True

            c_add = s2[r]
            counts2[c_add] = 1 + counts2.get(c_add, 0)
            if c_add in counts1:
                if counts1[c_add] == counts2[c_add]:
                    matches += 1
                elif counts1[c_add] + 1 == counts2[c_add]:
                    matches -= 1

            c_rem = s2[l]
            counts2[c_rem] -= 1
            if c_rem in counts1:
                if counts1[c_rem] == counts2[c_rem]:
                    matches += 1
                elif counts1[c_rem] - 1 == counts2[c_rem]:
                    matches -= 1

            l += 1

        return matches == len(counts1)