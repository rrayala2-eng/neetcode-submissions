from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for words in strs:
            dic["".join(sorted(words))].append(words)
        return list(dic.values())