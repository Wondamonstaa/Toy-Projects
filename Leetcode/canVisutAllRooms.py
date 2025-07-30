class Solution:

    def dfs(self, graph, node, visited=None):

        if node in visited:
            return 
        
        visited.add(node)

        for neighbor in graph[node]:
            self.dfs(graph, neighbor, visited)


    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return True

        visited = set()
        self.dfs(rooms, 0, visited)

        return len(visited) == len(rooms)
