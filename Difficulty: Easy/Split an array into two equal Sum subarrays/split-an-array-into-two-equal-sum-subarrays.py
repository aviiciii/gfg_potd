class Solution:
    def canSplit(self, arr):
        #code here
        front = {}
        back = {}
        sum_front = 0
        sum_back = 0
        j = len(arr) - 1
        for i in range(len(arr)):
            sum_front += arr[i]
            sum_back += arr[j-i]
            
            front[sum_front] = i
            back[sum_back] = j-i
            
        # print(front, back)
            
        for x in front.keys():
            if x in back.keys():
                if front[x] +1 == back[x]:
                    return True
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends