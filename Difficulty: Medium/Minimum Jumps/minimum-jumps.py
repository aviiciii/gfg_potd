#User function Template for python3
class Solution:
	def minJumps(self, arr):
        jumps = 0
        l = 0
        r = 0
        farthest = 0
	    
	   # first jump
        while r < len(arr)-1:
            
            for i in range(l,r+1):
                farthest = max(farthest, i+arr[i])
   
            # print(r, farthest)
            if farthest <= r:
                return -1
            l = r+1
            r = farthest
            jumps +=1
            
        return jumps
        
        
        # asdfasfd
        # if (nums.length == 1) return 0; 
        
        # int n = nums.length;
        # int l = 0, r = 0, jumps = 0, farthest = 0;

        # while (r <= n - 1) { 
         

        #     for (int i = l; i <= r; i++) {
        #         farthest = Math.max(farthest, i + nums[i]);
        #         if (farthest >= n - 1) { 
        #             return jumps + 1;
        #         }
        #     }
        #     l = r + 1;
        #     r = farthest;
        #     jumps++;
        # }

        # return jumps;
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends