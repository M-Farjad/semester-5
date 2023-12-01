def Iddfs(src, target, maxDepth):
    for i in range(maxDepth):
        if Dls(src, target, i):
            return True
    return False

def Dls(src, target, limit):
    if limit == 0 and src == target:
        return True
    if limit > 0:
        for i in range(len(src.adj)):
            if Dls(src.adj[i], target, limit-1):
                return True
    return False

class Node:
    def __init__(self, value):
        self.value = value
        self.adj = []

# main program
# construct the tree
root = Node('A')
root.adj.append(Node('B'))
root.adj.append(Node('C'))
root.adj.append(Node('D'))
root.adj[0].adj.append(Node('E'))

target = Node('E')
maxDepth = 2
if Iddfs(root, target, maxDepth):
    print("Target is reachable within max depth")
else:
    print("Target is not reachable within max depth")