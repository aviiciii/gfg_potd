#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


def reverseList(head):
    prev = None
    i = head

    while i != None:
        front = i.next
        i.next = prev
        prev = i
        i = front
    return prev

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        head = reverseList(head)
        i = head 
        carry = 1
        while i != None:
            
            value = i.data + carry
            if value < 10:
                
                i.data = value
                carry = 0
                break
            else:
                i.data = value%10
            prev = i
            i = i.next
            
        head = reverseList(head)
        
        if carry ==1:
            newNode = Node(1)
            newNode.next = head
            return newNode
        return head
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        for i in arr:
            list1.insert(i)

        resHead = Solution().addOne(list1.head)
        PrintList(resHead)
        print()

# } Driver Code Ends