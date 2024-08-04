class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    # def __str__(self):
    #     return f"[{self.start}, {self.end}]"
    # def __repr__(self):
    #     return f"[{self.start}, {self.end}]"
    

    
    

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings=[]
        for i in range(len(start)):
            meetings.append(Meeting(start[i],end[i]))
        meetings = sorted(meetings, key = lambda i: i.end)
        # print(meetings)
        end = -1
        count = 0
        
        for meeting in meetings:
            if meeting.start > end:
                end = meeting.end
                count += 1
        
        return count
        
        
        
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends