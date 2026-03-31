class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Create a graph and in-degree counter
        adj_list = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # Step 2: Build the graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Check for invalid case where prefix appears after the longer word
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            # Compare characters and build the graph
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Step 3: Topological Sort using Kahn's Algorithm
        zero_in_degree_queue = deque([char for char in in_degree if in_degree[char] == 0])
        topo_order = []
        
        while zero_in_degree_queue:
            char = zero_in_degree_queue.popleft()
            topo_order.append(char)
            
            # Decrease the in-degree of neighboring nodes
            for neighbor in adj_list[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)
        
        # If topological sort includes all characters, return the result
        if len(topo_order) == len(in_degree):
            return "".join(topo_order)
        else:
            return ""
     