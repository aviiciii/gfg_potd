#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        subsum = {
            
        }
        
        tot = 0
        if s < 0:
            return [-1]
        
        for i in range(n):
            
            tot += arr[i]
            
            
            if tot == s:
                return [1,i+1]
                
            if tot - s in subsum.keys() and i - subsum[tot-s] > -1:
                return [subsum[tot-s] +1 , i +1]
            subsum[tot]= i+1
                
        return [-1]
       #Write your code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends