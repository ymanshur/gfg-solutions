import heapq

class Solution:
    
    #Function to return the minimum cost to react at bottom
    #right cell from top left cell.
    def minimumCostPath(self, cost):
        m = len(cost)
        n = len(cost[0])
        
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = cost[0][0]
        
        path = [[""] * n for _ in range(m)]
        #path[0][0] = str(cost[0][0])
        
        dist_min_q = []
        heapq.heappush(dist_min_q, (dist[0][0], 0, 0))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while len(dist_min_q) > 0:
            _, x, y = heapq.heappop(dist_min_q)
            
            if x == m - 1 and y == n - 1:
                #print(path[x][y])
                return dist[x][y]
            
            for dir_x, dir_y in directions:
                x1 = x + dir_x
                y1 = y + dir_y
                if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n:
                    if dist[x1][y1] > dist[x][y] + cost[x1][y1]:
                        #path[x1][y1] = "%s->%d" % (path[x][y], cost[x1][y1])
                        dist[x1][y1] = dist[x][y] + cost[x1][y1]
                        heapq.heappush(dist_min_q, (dist[x1][y1], x1, y1))
        
        #print(path[m - 1][n - 1])
        return dist[m - 1][n - 1]