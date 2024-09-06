#User function Template for python3

class Solution:
    def maxOnes (self, Mat, N, M):
        # code here 
        min_zero = 9999999
        min_row = -1
       
        for row in range(N):
            
            cur_zero = 0
            
            
            for ele in range(M):
                if Mat[row][ele] == 0:
                    cur_zero += 1
                else:
                    break
                
                
            if cur_zero < min_zero:
                min_zero = cur_zero
                min_row = row
                
                
        return min_row
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
		c = int(size[1])
		line = list(map(int,input().split()))
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
        for i in range(r):
			for j in range(c):
				matrix[i][j] = line[i*c+j]
        ob = Solution()
        print(ob.maxOnes(matrix,r,c))

# } Driver Code Ends