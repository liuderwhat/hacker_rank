import sys

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

    # 用queue存每一個level中，leftc與rightc各自的child
    # 所以會用兩個if連續去存
    def levelOrder(self,root):
        #Write your code here
        if root :
            q = [root]
        else:
            q = []
        ans = []
        while q:

            node = q.pop(0)
            # end : 不換行
            print(node.data, end = ' ')

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
