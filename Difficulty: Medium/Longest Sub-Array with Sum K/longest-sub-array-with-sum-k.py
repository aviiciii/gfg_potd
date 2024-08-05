#User function Template for python3


class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        sum_dict = {}
        sum = 0
        long = 0 
        for i in range(n):
            sum += arr[i]
            if not sum in sum_dict.keys():
                sum_dict[sum] = i
            if sum == k and i+1 > long:
                long = i+1
            else:
                if sum-k in sum_dict.keys():
                    ind = sum_dict[sum-k]
                    if i - ind > long:
                        long = i - ind
        #     print(sum, long)
        # print(sum_dict)
        return long
        
            
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends