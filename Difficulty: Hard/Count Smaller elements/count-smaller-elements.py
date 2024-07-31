#User function Template for python3
from sortedcontainers import SortedList
class Solution:

	def constructLowerArray(self,arr):
		# code here
# 		res = [0]*len(arr)
		
# 		for i in range(len(arr)):
		    
# 		    for j in range(i, len(arr)):
# 		        if arr[j] < arr[i]:
# 		            res[i]+=1
		    
#        return res

        s = SortedList()
        res = []
        
        for i in arr[::-1]:
            ans = SortedList.bisect_left(s, i)
            res.append(ans)
            s.add(i)
            
        return res[::-1]
        
		    
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends