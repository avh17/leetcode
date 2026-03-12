class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            res = 1
            while q:
                qLen = len(q)
                for _ in range(qLen):
                    i, j = q.popleft()
                    for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                        if (0<=r<rows and 0<=c<cols and grid[r][c]==1):
                            q.append((r,c))
                            grid[r][c] = 0
                            res+=1

            return res

        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r,c))

        return area