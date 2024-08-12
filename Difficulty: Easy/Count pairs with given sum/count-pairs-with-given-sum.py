#User function Template for python3
import itertools

class Solution:
    def getPairsCount(self, arr, s):
        # # code here
        # comb = itertools.combinations(arr, 2)
        # count = 0
        # for i in comb:
        #     if i[0]+i[1] == s:
        #         count +=1
        # return count
        
        d = {
            
        }
        ans = 0
        for ele in arr:
            # print(d)
            com = s-ele
            
        
            if com in d:
                ans += d[com]
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1
            
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())

    while tc > 0:
        k = int(input().strip())
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.getPairsCount(arr, k)
        print(ans)

        tc -= 1

# } Driver Code Ends