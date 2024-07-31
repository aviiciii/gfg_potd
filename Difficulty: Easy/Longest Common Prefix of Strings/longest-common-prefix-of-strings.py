#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        phrase = ""
        smallest = min(arr)
        # print(smallest)
        for i in range(len(smallest)):
            ch = ""
            for ele in arr:
                if ch =="":
                    ch = ele[i]
                    
                elif ch==ele[i]:
                    pass
                else:
                    ch= -1
                    break
            if ch =="" or ch == -1:
                break
            else:
                phrase +=ch
                
        if phrase == "":
            return -1
        return phrase
                    
                
                    
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends