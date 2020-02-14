class Trie:
    """
    Implement Trie (Prefix Tree)
    Trie树，又叫字典树、前缀树（Prefix Tree）、单词查找树 或 键树，是一种多叉树结构
    https://blog.csdn.net/lisonglisonglisong/article/details/45584721
    """

    def __init__(self):
        self.root = {}

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        p = self.root
        for ch in word:
            if ch not in p:
                p[ch] = {}
            p = p[ch]
        p['#'] = '#'

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for ch in word:
            if ch in p:
                p = p[ch]
            else:
                return False

        if '#' in p:
            return True
        else:
            return False

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for ch in prefix:
            if ch in p:
                p = p[ch]
            else:
                return False
        return True


def classCall(className):
    def classMothd(classM, classarg):
        return className.classM(classarg)

    return classMothd


if __name__ == "__main__":
    a = ["insert", "search", "search", "startsWith", "insert", "search"]
    b = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    obj = Trie()
    ans = []
    for i, j in zip(a, b):
        if j:
            ans.append(obj.__getattribute__(i)(j[0]))
            # ans.append(getattr(obj,i,None)(j[0]))
        else:
            ans.append(obj.__getattribute__(i)())
            # ans.append(getattr(obj,i,None)())

    print(ans)
