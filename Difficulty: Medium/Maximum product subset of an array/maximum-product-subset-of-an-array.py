#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        
        MOD = 10**9 +7
        # Write your code here
        if len(arr) == 1:
            return arr[0]
        
        # take lowest even negatives
        arr.sort()
        
        negatives = [x for x in arr if x < 0]
        positives = [x for x in arr if x > 0]
        
        if negatives or positives:
            
            if positives or len(negatives) >1:
                if len(negatives) % 2 != 0:
                    negatives.pop()
            
            res = 1
                
            for ele in negatives:
                res *= ele
                
            for ele in positives:
                res *= ele
                
            if res < 0 and 0 in arr:
                return 0
        else:
            return 0
        
        
        # take all positives
        return res % MOD
            
        
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends