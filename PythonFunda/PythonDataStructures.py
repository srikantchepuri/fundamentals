#Stacks using lists
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)==0:
            return False
        else:
            self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return False
        else:
            return self.stack[len(self.stack)-1]


class Queue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.start=0
        self.end=-1
        self.Q=[None]*capacity
        self.size=0
    def isFull(self):
        return self.capacity==self.size
    def isEmpty(self):
        return self.size==0
    def enQueue(self,item):
        if self.isFull():
            print("Queue Full")
            return False
        else:
            self.end=(self.end+1)%self.capacity
            self.Q[self.end]=item
            self.size+=1
            print("Enqueued")
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
            return False
        else:
            self.start=(self.start+1)%self.capacity
            self.size-=1
    def frontQueue(self):
        if self.isEmpty():
            print("Queue Empty")
            return False
        else:
            return self.Q[self.start]
    

#Linked List

class LinkedList:
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    def __init__(self):
        self.head=None
    def traverse(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def push(self,node):
        thead=self.head
        self.head=node
        self.head.next=thead
    def lastnode(self):
        temp=self.head
        while temp and temp.next :
            temp=temp.next
        return temp
    def append(self,node):
        self.lastnode().next=node



#Tree Implrementation
#root, parent, children, leaves
'''
Binary Tree: A tree whose elements have at most 2 children is called a binary tree.
Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
The maximum number of nodes at level ‘l’ of a binary tree is 2**(l-1).
Maximum number of nodes in a binary tree of height ‘h’ is 2**h – 1.
In Binary tree where every node has 0 or 2 children, number of leaf nodes is always one more than nodes with two children.
Full Binary Tree A Binary Tree is full if every node has 0 or 2 children
Complete Binary Tree: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible

Balanced Binary Tree
A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. 
For Example, AVL tree maintains O(Log n) height by making sure that the difference between 
heights of left and right subtrees is 1. Red-Black trees maintain O(Log n) height by making sure 
that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. 

Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, 
insert and delete.



'''
# Python program to for tree traversals 

# A class that represents an individual node in a 
# Binary Tree 
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
		print(root.val), 

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
		print(root.val), 


# A function to do preorder tree traversal 
def printPreorder(root): 

	if root: 

		# First print the data of node 
		print(root.val), 

		# Then recur on left child 
		printPreorder(root.left) 

		# Finally recur on right child 
		printPreorder(root.right) 


# Driver code 
root = Node(1) 
root.left	 = Node(2) 
root.right	 = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print "Preorder traversal of binary tree is"
printPreorder(root) 

print "\nInorder traversal of binary tree is"
printInorder(root) 

print "\nPostorder traversal of binary tree is"
printPostorder(root) 



import sys

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
    def printSolution(self,dist):
        print("vertex distance from source")
        for node in range(self.V):
            print(node,"t",dist[node])
    
    def minDistance(self,dist,sptSet):
        min=sys.maxsize
        for v in range(self.V):
            if dist[v]<min and sptSet[v]==False:
                min=dist[v]
                min_index = v
        
        return min_index

    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptSet=[False]*self.V

        for count in range(self.V):
            u=self.minDistance(dist,sptSet)
            sptSet[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and sptSet[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]
        self.printSolution(dist)


g  = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 
  
g.dijkstra(0); 