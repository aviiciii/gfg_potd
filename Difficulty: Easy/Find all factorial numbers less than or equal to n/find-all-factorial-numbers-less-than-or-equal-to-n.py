#User function Template for python3

def factorial(n):
    if n==0:
	    return 1
	
    return n * factorial(n-1)

class Solution:
    def factorialNumbers(self, n):
        ans=[]
    	#code here 
    	for i in range(1,n+1):
    	    f = factorial(i)
    	    if f > n:
    	        break
    	    ans.append(f)
        return ans
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends