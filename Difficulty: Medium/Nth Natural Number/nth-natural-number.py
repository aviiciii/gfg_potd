#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        res = ""
        while n > 0:
            r = n%9
            res = str(r)+res
            n = n//9
        return res
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends