# ----------------------------------- Binary Indexed Tree -----------------------------------
class BIT:
    def __init__(self, N: int):
        self.stree = [-1] * (N + 1)
    
    def change(self, i, x):
        while i < len(self.stree):
            self.stree[i] = max(x, self.stree[i])
            i |= (i + 1)
    
    def query(self, i):
        s = -1

        while i >= 0:
            s = max(s, self.stree[i])
            i &= i + 1
            i -= 1
        
        return s

# ----------------------------------- Trie -----------------------------------
class Trie:
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def delete(self, word, prune=False):
        current_dict = self.root
        nodes = [current_dict]
        objects = []
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
            objects.append(current_dict)

        del current_dict["_end_"]

        if prune:
            # https://leetcode.com/problems/maximum-genetic-difference-query/discuss/1344900/
            for c, obj in zip(word[::-1], objects[:-1][::-1]):
                if not obj[c]:
                    del obj[c]
                else:
                    break

        # assert word not in self  # confirm that the number has been removed

# ----------------------------------- Trie -----------------------------------
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.hasEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for x in word:
            curr = curr.children[x]
        
        curr.hasEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for x in word:
            if x not in curr.children:
                return False
            
            curr = curr.children[x]
        
        return curr.hasEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for x in prefix:
            if x not in curr.children:
                return False
            
            curr = curr.children[x]
        
        return True
    
# ----------------------------------- Segment Tree -----------------------------------
class SegmentTree:
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SegmentTree.py
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(
                self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop): # stop not inclusive``
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

class LazySegmentTree:
    def __init__(self, low, high, val):
        self.low = low
        self.high = high
        self.val = val
        self.lazy = 0
        self.left = None
        self.right = None
    
    def _extend(self):
        if self.low < self.high:
            if self.left is None:
                mid = (self.low + self.high) // 2
                self.left = LazySegmentTree(self.low, mid, self.val)
                if mid + 1 <= self.high:
                    self.right = LazySegmentTree(mid + 1, self.high, self.val)
            elif self.lazy != 0:
                self.left.val += self.lazy
                self.left.lazy += self.lazy
                self.right.val += self.lazy
                self.right.lazy += self.lazy
        self.lazy = 0
        
    def update(self, low, high, delta): # [low, high] inclusive
        if low > high or self.high < low or high < self.low:
            return
        if low <= self.low and self.high <= high:
            self.val += delta
            self.lazy += delta
            return
        self._extend()
        self.left.update(low, high, delta)
        self.right.update(low, high, delta)
        self.val = max(self.left.val, self.right.val)
    
    def query(self, low, high):  # [low, high] inclusive
        if low > high or self.high < low or high < self.low:
            return 0
        if low <= self.low and self.high <= high:
            return self.val
        self._extend()
        return max(self.left.query(low, high), self.right.query(low, high))
