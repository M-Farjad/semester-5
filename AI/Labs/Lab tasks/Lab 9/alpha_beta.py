class TreeNode:
  def _init_(self, value, children=None):
    self.value = value
    self.children = children if children is not None else []
    self.is_maximizing = True

def minimax(node ,depth , is_maximizing):
  if depth == 0 or not node.children:
    return node.value

  if is_maximizing:
    max_eval = -float('inf')
    for child in node.children:
      eval = minimax(child, depth -1 ,False)
      max_eval = max(max_eval, eval)
    return max_eval
  else:
    min_eval = float('inf')
    for child in node.children:
      eval = minimax(child, depth-1 , True)
      min_eval = min(min_eval, eval)
    return min_eval

root = TreeNode(1)
node1 = TreeNode(3)
node2 = TreeNode(-4)
node3 = TreeNode(3)
node4 = TreeNode(5)
node5 = TreeNode(-4)
node6 = TreeNode(9)
node7 = TreeNode(-1)
node8 = TreeNode(3)
node9 = TreeNode(5)
node10 = TreeNode(1)
node11 = TreeNode(-6)
node12 = TreeNode(-4)
node13 = TreeNode(0)
node14 = TreeNode(9)

root.children = [node1, node2]
node1.children = [node3, node4]
node2.children =[node5, node6]
node3.children =[node7, node8]
node4.children =[node9, node10]
node5.children =[node11, node12]
node6.children =[node13, node14]



def minimax_with_pruning(node, depth, alpha, beta, is_maximizing):
    if depth == 0 or not node.children:
        return node.value

    if is_maximizing:
        max_eval = -float('inf')
        for child in node.children:
            eval = minimax_with_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune the branch
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax_with_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune the branch
        return min_eval

# best_value = minimax(root, depth=4, is_maximizing=True)
best_value = minimax_with_pruning(root, depth=4, alpha=-float('inf'), beta=float('inf'), is_maximizing=True)

print(best_value)