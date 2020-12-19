# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if not root.left:
            return right + 1
        if not root.right:
            return left + 1
        return max(left, right) + 1
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root, result):
            if root is not None:
                inorder(root.left, result)
                result.append(root.val)
                inorder(root.right, result)
                
        def previsit(root, result):
            if root is not None:
                result.append(root.val)
                previsit(root.left, result)
                previsit(root.right, result)
                
        def postvisit(root, result):
            if root is not None:
                postvisit(root.left, result)
                postvisit(root.right, result)
                result.append(root.val)
                
        result = []
        inorder(root, result)
        return result
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
class Solution:
    def invert(self, node):
            node.right, node.left = node.left, node.right
            if node.left:
                self.invert(node.left)
            if node.right:
                self.invert(node.right)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.invert(root)
        return root
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/ 

```python
class Solution:
    def DFS(self, node, res, level):
            if node is None:
                return 0
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            self.DFS(node.left, res, level + 1)
            self.DFS(node.right, res, level + 1)
            
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.DFS(root, res, 0)
        return res
```