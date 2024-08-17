#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        output = [0] * len(nums)
        
        total = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros+= 1
            else:
                total *= i
            
        
        for i in range(len(nums)):
            if zeros == 1:
                if nums[i] == 0:
                    output[i]= int(total)
                else:
                    output[i] =0
                continue
            if zeros >1:
                break
            
            
            
            output[i] = int(total / nums[i])
            
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends