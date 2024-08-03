#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        temp = -1
        for i in arr:
            if i > temp:
                temp = i
        while temp in arr:
            arr.remove(temp)
        temp = -1
        if arr:
            for i in arr:
                if i > temp:
                    temp = i
        return temp


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends