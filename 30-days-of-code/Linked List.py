'''
STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1

2 3 4 1

4
2
3
4
1
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        node = Node(data)
        if not head :
            return node
        else:
            tail = head
            while tail.next:
                tail = tail.next
            head.next = node
            return head
        
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);     