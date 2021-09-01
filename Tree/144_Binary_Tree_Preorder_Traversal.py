# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/1403244/3-Simple-Python-solutions
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = [root]
        
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                stack.append(temp.right) #as we are using stack which works on LIFO, we need to push right tree first so that left will be popped out
                stack.append(temp.left)
                
        return ans