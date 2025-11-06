# class Node:

# 	def __init__(self, data):
# 		self.left = None
# 		self.right = None
# 		self.data = data

# 	def insert(self, data):
# 		# Compare the new value with the parent node
# 		if self.data:
# 			if data < self.data:
# 				if self.left is None:
# 					self.left = Node(data)
# 				else:
# 					self.left.insert(data)
# 		elif data > self.data:
# 			if self.right is None:
# 				self.right = Node(data)
# 			else:
# 				self.right.insert(data)
# 		else:
# 			self.data = data


# # Print the tree
# 	def PrintTree(self):
# 		if self.left:
# 			self.left.PrintTree()
# 		print( self.data)
# 		if self.right:
# 			self.right.PrintTree()
	
# 	def size(node):
# 		if node is None:
# 			return 0
# 		else:
# 			return (size(node.left)+ 1 + size(node.right))



# # Use the insert method to add nodes
# # root = Node(12)
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left  = Node(4)
# root.left.right = Node(5)
# # root.insert(6)
# # root.insert(14)
# # root.insert(3)
# # root.PrintTree()
# size(root)

# Python Program to find the size of binary tree

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Computes the number of nodes in tree
def size(node):
	if node is None:
		return 0
	else:
		return (size(node.left)+ 1 + size(node.right))

def maxnode(node):
    if node is None:
        return
    lm = maxnode(node.left)
    rm = maxnode(node.right)
    m = max(max(lm,rm),node.data)
    
    return m
    


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Size of the tree is %d" %(size(root)))
print("max node of the tree is %d" %(maxnode(root)))

