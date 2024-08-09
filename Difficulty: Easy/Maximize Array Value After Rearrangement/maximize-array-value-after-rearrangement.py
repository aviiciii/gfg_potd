#User function Template for python3
MOD = (10 ** 9) + 7
class Solution:
    def Maximize(self, a): 
        # Complete the function
        a.sort()
        sum = 0
        for i, ele in enumerate(a):
            sum += (ele * i)
        return sum % MOD



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends