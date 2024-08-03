class Solution:
    def celebrity(self, mat):
        # code here
        n= len(mat)
        
        knows = [0]*n
        is_known = [0]*n
        
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if mat[i][j] == 1:
                    knows[i] += 1
                    is_known[j] +=1
                    
        
                    
        for i in range(n):
            if knows[i]==0 and is_known[i]==n-1:
                return i
                
        return -1
        
                

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends