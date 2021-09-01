# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/1377979/ororshort-and-sweet-oror-python-oror-beginner-friendly
class Solution:
    def inorderTraversal(self, root):
        
        ans=[]
        
        def dfs(node):
            
            if not node:
                return 
            
            dfs(node.left)
            
            ans.append(node.val)
            
            dfs(node.right)
        
        dfs(root)
        return ans