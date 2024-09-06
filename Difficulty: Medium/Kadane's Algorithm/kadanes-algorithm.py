#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        i = 0
        maxi = None
        cur = 0
        
        while i < len(arr):
            
            cur += arr[i]
            # print(arr[i], cur)
            
            if maxi == None:
                maxi = cur
            elif cur> maxi:
                maxi = cur
                
            if cur <0:
                cur = 0
            
            i+=1
            
        return maxi
                
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends