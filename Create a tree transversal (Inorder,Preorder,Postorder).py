# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:42:28 2020

@author: sony
"""
#purahar reddy, 22
#Create a tree transversal (Inorder,Preorder,Postorder)
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val) 
  
        # now recur on right child 
        printInorder(root.right)
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val) 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val) 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right)
# Driver code 
root = Node(1)


root.left = Node(5)
root.left.left = Node(9)
root.left.right = Node(2)
root.right = Node(87)
root.right.right = Node(45)
root.right.left = Node(10)
root.left.left.left = Node(7)
root.left.right.right = Node(65)
root.right.right.right = Node(74)
root.right.left.left = Node(56)
print("Preorder traversal of binary tree is")
printPreorder(root) 
  
print("Inorder traversal of binary tree is")
printInorder(root) 
  
print("Postorder traversal of binary tree is")
printPostorder(root)
