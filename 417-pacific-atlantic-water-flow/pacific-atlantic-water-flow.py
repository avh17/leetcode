class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        p_que = deque()
        a_que = deque()


        p_set = set()
        a_set = set()

        for j in range(n):
            p_que.append((0, j))
            p_set.add((0, j))

        for i in range(1, m):
            p_que.append((i, 0))
            p_set.add((i, 0))

        for i in range(m):
            a_que.append((i, n-1))
            a_set.add((i, n-1))

        for j in range(n-1):
            a_que.append((m-1,j))
            a_set.add((m-1,j))
        
        def get_coords(que, seen):
            coords = set()
            while que:               
                qLen = len(que)
                for _ in range(qLen):
                    i, j = que.popleft()
                    coords.add((i, j))
                    for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                        if (0<=r<m and 0<=c<n and (r,c) not in seen and heights[r][c]>=heights[i][j]):
                            seen.add((r,c))
                            que.append((r,c))

            return coords

        p_coords = get_coords(p_que, p_set)
        a_coords = get_coords(a_que, a_set)

        return list(p_coords.intersection(a_coords))