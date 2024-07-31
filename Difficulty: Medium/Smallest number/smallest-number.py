#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
def sod(n):
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
class Solution:
    
        
    def smallestNumber(self, s, d):
        # code here
        res = int("1"+"0"*(d-1))
        m = int("9" * d)
        ans = False
        while res <= m:
            if sod(res) == s:
                ans = True
                break
            res += 1
           
            
        if ans:
            return res
        else:
            return -1
        
        

#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends