# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/symmetric-tree/discuss/1408213/Python-oror-easy-recursion-solution
class Solution:
	def isSymmetric(self, root):

		def fun(root1, root2):
			if root1 is None and root2 is None:
				return True
			if root1 is None or root2 is None:
				return False

			if root1.val == root2.val:
				x = fun(root1.left, root2.right)
				y = fun(root1.right, root2.left)

				if x == True and y == True:
					return True
				return False
			return False


		if root is None:
			return True

		return fun(root, root)
        