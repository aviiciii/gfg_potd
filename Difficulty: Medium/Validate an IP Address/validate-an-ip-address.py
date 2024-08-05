#User function Template for python3

class Solution:
    def isValid(self, str):
        #code here
        try:
            values = list(map(int, str.split('.')))
            for i in values:
                if not( i >-1 and i<256):
                    return False
            return True
        except:
            return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends