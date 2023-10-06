class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True

        self.dfs(rooms, 0, visited)

        for v in visited:
            if not v:
                return False
    
        return True 
    
    def dfs(self, rooms, ind, visited):
        for i in rooms[ind]:
            if not visited[i]:
                visited[i] = True
                self.dfs(rooms, i, visited)


        