class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        l = 0
        r = len(arr)-1
        i = 0
        
        while i<=r:
            if arr[i] == 0:
                if i ==l:
                    i +=1
                    continue
                    
                arr[i], arr[l] = arr[l], arr[i]
                l+=1
                
                
            elif arr[i]==2:
                arr[i], arr[r] = arr[r], arr[i]
                r-=1
                
                
            else:
                i +=1
            
        return arr


#User function Template for python3

# class Solution:
#     def sort012(self,arr,n):
#         # code here
#         l = 0 
#         r = n-1
#         i = 0
#         while i <= r:
            
#             if arr[i] == 0:
                
#                 if l == i:
#                     i += 1
#                     continue
                
#                 arr[i], arr[l] = arr[l], arr[i]
#                 l += 1
                
#             elif arr[i] == 2:
                
#                 arr[r], arr[i] = arr[i], arr[r]
#                 r -=1
#             else:
#                 i +=1
            
                
#         return arr


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends