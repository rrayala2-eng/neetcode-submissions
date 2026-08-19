class TrieNode:
    def __init__(self):
        self.childern = {}
        self.endOfWord = False
    

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.childern:
                curr.childern[c] = TrieNode()
            curr = curr.childern[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):

                c = word[i]

                if c == ".":
                    for child in curr.childern.values():
                        if dfs(i + 1, child):
                            return True
                    return False


                else:
                    if c not in curr.childern:
                        return False
                    curr = curr.childern[c]
            return curr.endOfWord
        
        return dfs(0, self.root)

        
        
        

