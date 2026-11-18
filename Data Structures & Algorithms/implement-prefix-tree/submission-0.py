class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = Node()
                node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        s = []
        s.append(node)
        while s:
            cur = s.pop()
            if cur.is_word:
                return True
            for nd in cur.children.values():
                s.append(nd)
        return False



        
        