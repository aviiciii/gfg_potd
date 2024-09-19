# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        # code here 
        strings = S.split('.')
        res = ""
        for i in range(len(strings)-1, -1, -1):
            res += strings[i] + "."
        return res.rstrip('.')


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends