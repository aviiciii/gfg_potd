#User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        for i in range(len(arr)):
            if i == 0 :
                if len(arr)>1 and arr[i] != arr[i+1]:
                    
                    return arr[i]
                elif len(arr) == 1:
                    return arr[i]
            elif i == len(arr)-1 and arr[i-1] != arr[i]:
                return arr[i]
            elif arr[i-1] != arr[i] and arr[i] != arr[i+1]:
                return arr[i]
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends