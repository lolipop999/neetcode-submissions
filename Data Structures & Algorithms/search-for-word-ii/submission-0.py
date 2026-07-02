class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # take all the words and turn them into TrieNode
        root = TrieNode()
        cur = root

        for i, word in enumerate(words):
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
            cur = root
        
        res = set()
        visited = set()
        def dfs(r, c, node, wordSoFar):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or (r, c) in visited or board[r][c] not in node.children:
                return
            node = node.children[board[r][c]]
            wordSoFar += board[r][c]
            visited.add((r, c))
            if node.endOfWord:
                res.add(wordSoFar)
            dfs(r+1, c, node, wordSoFar)
            dfs(r-1, c, node, wordSoFar)
            dfs(r, c+1, node, wordSoFar)
            dfs(r, c-1, node, wordSoFar)
            visited.remove((r, c))

        # run DFS starting at every part of board
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, root, "")
        return list(res)
        

        

        