from collections import Counter

class Solution:
    
    def dfs(self, graph, node, calls, visited=None):
        
        if node in visited:
            return

        visited.add(node)
        calls[0] += 1

        for neighbor in graph[node]:
            self.dfs(graph, neighbor, calls, visited)
     
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        if not isConnected:
            return 0

        visited = set()
        calls = [0]
        adj_list = {}
        provinces = 0

        for i in range(len(isConnected)):
            adj_list[i] = []
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        
        for node in range(len(isConnected)):
            if node not in visited:
                self.dfs(adj_list, node, calls, visited)
                provinces += 1

        return provinces
