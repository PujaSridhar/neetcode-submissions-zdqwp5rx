class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board, words):
        def backtrack(row, col, parent):
            letter = board[row][col]
            curr_node = parent.children[letter]
            
            # check if there is any match
            if curr_node.word is not None:
                result.add(curr_node.word)
                curr_node.word = None
            
            # mark the current cell as visited
            board[row][col] = '#'
            
            # explore the neighbors in 4 directions: up, right, down, left
            for (r, c) in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] in curr_node.children:
                    backtrack(r, c, curr_node)
            
            # end of exploration, restore the original letter in the board
            board[row][col] = letter
            
            # Optimization: incrementally remove the leaf nodes
            if not curr_node.children:
                parent.children.pop(letter)

        # Step 1). Construct the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # Step 2). Backtracking starting for each cell in the board
        ROWS, COLS = len(board), len(board[0])
        result = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in trie.root.children:
                    backtrack(row, col, trie.root)
        
        return list(result)