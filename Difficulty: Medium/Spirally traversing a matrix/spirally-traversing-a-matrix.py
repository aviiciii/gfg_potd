class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        
        
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if not (left < right and top < bottom):
                break
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            if not (left < right and top < bottom):
                break
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left +=1
            
                
            
            
        
        

        return res
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends