'''
7
3
5
2
1
4
6
7

3
'''
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here

        if root is None:

            return -1

        else:

            l_height = (1 + self.getHeight(root.left))
            r_height = (1 + self.getHeight(root.right))

            if l_height >= r_height:
                return l_height
            else:
                return r_height
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       