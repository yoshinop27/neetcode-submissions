class TreeMap:

    class Node:
        
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.insertNodeH(self.root, key, val)
    
    # HELPER
    def insertNodeH(self, cur, key, val):
        if not cur:
            return self.Node(key, val)
        
        if key < cur.key:
            cur.left = self.insertNodeH(cur.left, key, val)
        elif key > cur.key:
            cur.right = self.insertNodeH(cur.right, key, val)
        else:
            cur.val = val
        
        return cur

    def get(self, key: int) -> int:
        cur = self.root
        while cur and cur.key != key:
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        if not cur:
            return -1
        return cur.val

    def getMin(self) -> int:
        if not self.root:
            return -1 

        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        self.root = self.removeH(key, self.root)

    # HELPER
    def removeH(self, key, cur):
        if not cur:
            return
        if key < cur.key:
            cur.left = removeH(key, cur.left)
        elif key > cur.key:
            cur.right = removeH(key, cur.right)
        else:
            if not (cur.left and cur.right):
                if cur.left:
                    return cur.left
                else:
                    return cur.right
            else:
                # Switch
                nodeToReplace = self.findMin(cur.right)
                cur.val = nodeToReplace.val
                cur.key = nodeToReplace.key
                # Remove Duplicate
                cur.right = self.removeH(cur.key, cur.right)
                return cur

    # HELPER
    def findMin(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur

    def getInorderKeys(self) -> List[int]:
        lst = []
        if not self.root:
            return lst
        return self.ioH(self.root, lst)

    # HELPER 
    def ioH(self, cur, lst):
        if not cur:
            return
        self.ioH(cur.left, lst)
        lst.append(cur.key)
        self.ioH(cur.right, lst)
        return lst
        

