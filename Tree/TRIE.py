class Trie:
    head = {}

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch]={}
            cur = cur[ch]
        cur['*'] = True
        