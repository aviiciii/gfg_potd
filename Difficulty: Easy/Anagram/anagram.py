#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        d = {}
        
        for letter in a:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        
        for letter in b:
            if letter in d:
                if d[letter]>0:
                    d[letter]-=1
                else:
                    return False
            else:
                return False
        
        for letter in d:
            if d[letter]>0:
                return False
        
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends