class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        islands = 0

        def dfs(visited, graph, root):
            if root not in visited: # if this node hasn't been visited
                # print(visited)
                visited.add(root)
                # explore the neighbors of root in the matrix using a right, left, bottom, top, appraoch
                if (root[1]+1) < len(grid[root[0]]) and graph[root[0]][root[1]+1] == "1": # if there is a right neighbour of 1
                    dfs(visited, graph, (root[0],root[1]+1))
                if (root[1]-1) >= 0 and graph[root[0]][root[1]-1] == "1": # if there is a left neighbour of 1
                    dfs(visited, graph, (root[0],root[1]-1))
                if (root[0]+1) < len(grid) and graph[root[0]+1][root[1]] == "1": # if there is a bottom neighbour of 1
                    dfs(visited, graph, (root[0]+1,root[1]))
                if (root[0]-1) >= 0 and graph[root[0]-1][root[1]] == "1": # if there is a top neighbour of 1
                    dfs(visited, graph, (root[0]-1,root[1]))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print((i, j))
                if (i, j) not in visited and grid[i][j] == "1":
                    islands += 1
                    dfs(visited, grid, (i, j))
        
        # print(visited)
        return islands

        