#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        if n > 0:
            print("GFG", end = " ")
            self.printGfg(n-1)
        return


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
# } Driver Code Ends