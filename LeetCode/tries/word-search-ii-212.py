from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False
        self.refs = 0

    def add_word(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.end_of_word = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if(r < 0 or c < 0 or r == rows or c == cols or
               (r, c) in visit or board[r][c] not in node.children or
               (node.children[board[r][c]].refs < 1)):
                return
            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end_of_word:
                node.end_of_word = False
                res.add(word)
                root.removeWord(word)

            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)


word2 = Solution()
print(word2.findWords([["o", "a", "a", "n"],
                       ["e", "t", "a", "e"],
                       ["i", "h", "k", "r"],
                       ["i", "f", "l", "v"]],
                      ["oath", "pea", "eat", "rain"]))
