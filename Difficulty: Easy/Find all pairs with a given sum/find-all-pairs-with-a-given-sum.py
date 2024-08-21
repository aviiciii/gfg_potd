#User function Template for python3

class Solution:
    def allPairs(self, x, arr1, arr2):
        # Your code goes here 
        d = {
            
        }
        sum = 0
        for i in range(len(arr2)):
            d[arr2[i]] = i
        # print(d)
        res=[]
        for i in range(len(arr1)):
            key = x-arr1[i]
            if key in d:
                res.append([arr1[i], arr2[d[key]]])
        
        res = sorted(res, key = lambda x: x[0])        
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        arr1 = [int(x) for x in input().strip().split()]
        arr2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        answer = ob.allPairs(x, arr1, arr2)
        sz = len(answer)

        if sz == 0:
            print(-1)

        else:

            for i in range(sz):
                if i == sz - 1:
                    print(*answer[i])
                else:
                    print(*answer[i], end=', ')

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends