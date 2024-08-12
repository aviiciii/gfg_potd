#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        l = 0 
        r = n-1
        i = 0
        while i <= r:
            
            if arr[i] == 0:
                
                if l == i:
                    i += 1
                    continue
                
                arr[i], arr[l] = arr[l], arr[i]
                l += 1
                
            elif arr[i] == 2:
                
                arr[r], arr[i] = arr[i], arr[r]
                r -=1
            else:
                i +=1
            
                
        return arr
            
                    
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends