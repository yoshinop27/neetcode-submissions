class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch] 
            else:
                node.children[ch] = Node()
                node = node.children[ch]
        node.is_word = True         

    def search(self, word: str) -> bool:
        def rec_search(node, word):
            for i,ch in enumerate(word):
                if ch == '.':
                    # launch recursive search in all directions
                    for nd in node.children.values():
                        if rec_search(nd, word[i+1:]):
                            return True
                    return False
                if ch in node.children:
                    node = node.children[ch] 
                else:
                    return False
            return node.is_word
        return rec_search(self.root, word)
