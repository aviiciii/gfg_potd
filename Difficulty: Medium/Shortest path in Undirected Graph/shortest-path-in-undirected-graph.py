#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
    
        distance = [float('inf')] * n
        distance[src] = 0
    
        queue = deque([src])
    
        while queue:
            node = queue.popleft()
    
            for neighbor in adj[node]:
                if distance[node] + 1 < distance[neighbor]:
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
    
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1
    
        return distance


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends