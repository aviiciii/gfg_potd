from typing import List

class Solution:
    
    def solve(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], move: str, vis: List[List[int]], di: List[int], dj: List[int]):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        dir = "DLRU"
        for ind in range(4):
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1:
                vis[i][j] = 1
                self.solve(nexti, nextj, a, n, ans,
                           move + dir[ind], vis, di, dj)
                vis[i][j] = 0
    
    
    
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        ans = []
        n = len(m)
        vis = [[0 for _ in range(n)] for _ in range(n)]
        di = [+1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        
        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", vis, di, dj)
        return ans


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends