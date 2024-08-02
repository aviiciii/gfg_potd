class Solution:
	def editDistance(self, str1, str2):
		# Code here
        dp = [[float("inf")] * (len(str2) + 1) for _ in range(len(str1)+1)]
        
        for i in range(len(str2) +1):
            dp[-1][i] = len(str2) -i
            
        for i in range(len(str1) +1):
            dp[i][-1] = len(str1) -i
            
            
        for i in range(len(str1)-1, -1, -1):
            for j in range(len(str2)-1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+ min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        
        # for i in dp:
        #     print(i)
        return dp[0][0]
        
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends