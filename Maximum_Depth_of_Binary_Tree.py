class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class TreeSolutions:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
            
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    sol = TreeSolutions()
    depth = sol.maxDepth(root)
    inorder = sol.inorder_traversal(root)
    
    print("Maximum depth of the binary tree is:", depth)
    print("Inorder traversal of the binary tree is:", inorder)
    