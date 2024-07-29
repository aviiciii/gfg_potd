#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		
		flag = False
		ind=0
		
		for i,c in enumerate(s):
		    if c == ch:
		        if count == 1:
		            
    		        flag = True
    		        ind = i
    		        break
    		    else:
    		        count -=1
		    
	    if flag == False:
	        return ""
        else:
            return s[ind+1:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends