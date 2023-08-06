class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['*'] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return '*' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
