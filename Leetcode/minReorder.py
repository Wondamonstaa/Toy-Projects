class Solution:

    def dfs(self, graph, node, visited, count):

        visited.add(node)

        for neighbor, direction in graph[node]:
            if neighbor not in visited:
                if direction == 1:
                    count[0] += 1
                self.dfs(graph, neighbor, visited, count)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        visited = set()
        count = [0]
        adj_list = defaultdict(list)

        for a, b in connections:
            adj_list[a].append((b, 1)) # Forward direction
            adj_list[b].append((a, 0)) # Reverse

        # for node in range(len(adj_list)):
        #     if node not in visited:
        #         self.dfs(adj_list, node, visited, count)

        self.dfs(adj_list, 0, visited, count)

        return count[0]
