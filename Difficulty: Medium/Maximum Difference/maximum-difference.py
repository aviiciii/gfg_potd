class Solution:
    def findMaxDiff(self, arr):
        # code here
        
        ls = [0] * len(arr) 
        rs = [0] * len(arr)
        
        stack = []
        
        for i, ele in enumerate(arr):
            if stack:
                while stack:
                    if stack[-1] < ele :
                        ls[i] = stack[-1]
                        break
                        
                    else:
                        stack.pop()
                stack.append(ele)
                
                    
            else:
                stack.append(ele)
                
        stack = []
        
        for i, ele in enumerate(reversed(arr)):
            if stack:
                while stack:
                    if stack[-1] < ele :
                        rs[i] = stack[-1]
                        break
                        
                    else:
                        stack.pop()
                stack.append(ele)
                
                    
            else:
                stack.append(ele)
                
        rs=list(reversed(rs))
        maxi = 0
        for i in range(len(ls)):
            if abs(ls[i] - rs[i])> maxi:
                maxi = abs(ls[i] - rs[i])
                
            
            
        
        
        return maxi


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends