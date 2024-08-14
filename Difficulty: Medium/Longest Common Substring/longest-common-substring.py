#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        n = len(str1)
        m = len(str2)
        
        dp = [[0] * (m+1) for x in range(n+1)]
        # print(dp)
        
        for i in range(n):
            for j in range(m):
                
                if str1[i] == str2[j]:
                    dp[i+1][j+1] += dp[i][j] + 1
        maxi = 0
        for i in dp:
            cur = max(i)
            if cur> maxi:
                maxi = cur
        return maxi
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends