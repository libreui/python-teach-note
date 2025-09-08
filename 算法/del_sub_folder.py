from pprint import pprint


class Trie:
    def __init__(self):
        self.children = {}
        self.fid = -1

    def insert(self, i, f):
        node = self
        ps = f.split('/')
        for p in ps[1:]:
            if p not in node.children:
                node.children[p] = Trie()
            node = node.children[p]
        node.fid = i

    def search(self):
        def dfs(root):
            if root.fid != -1:
                ans.append(root.fid)
                return
            for child in root.children.values():
                dfs(child)

        ans = []
        dfs(self)
        return ans


class Solution:
    def removeSubfolders(self, folder) -> list:
        trie = Trie()
        for i, f in enumerate(folder):
            trie.insert(i, f)
        return [folder[i] for i in trie.search()]


if __name__ == '__main__':
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    s = Solution()
    print(s.removeSubfolders(folder))

