class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def rBfs(root):
    if(root==None):
        return
    print(root.value,end='->')
    rBfs(root.left)
    rBfs(root.right)

def rDfs(root):
    if(root==None):
        return
    rDfs(root.right)
    rDfs(root.left)
    print(root.value,end='->')
    
# Example usage:
# Constructing a simple binary tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("\nDFS ",end=''),
rDfs(root)
print("\nBFS ",end=''),
rBfs(root)

# Question 1:
#Ask the user to enter a value and search it in the above tree and print found or not found
inp = int(input("\nEnter a value to search: "))
found = False
def search(root,inp):
    global found
    if(root==None):
        return
    if(root.value==inp):
        found = True
        return
    search(root.left,inp)
    search(root.right,inp)
search(root,inp)
if(found):
    print("Found")
else:
    print("Not Found")


# Question 2:
# Use the above code to implement the depth limited search limit is 2
print("\nDFS limited to 2 ",end=''),
rDfs(root.left)
print("\nBFS limited to 2 ",end=''),
rBfs(root.left)

