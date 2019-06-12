'''
Need to use log(n) time complexity to solve this problem
'''

class TreeNode:
    	def __init__(self, val=None):
		self.val = val
		self.left, self.right = None, None

	@classmethod
	def genFullBinaryTree(cls, data):
		if not data:
			return None

		root = TreeNode(data[0])
		queue, index = [root], 0
		isLeft = True
		for val in data[1:]:
			node = queue[index]
			nNode = TreeNode(val)
			if isLeft:
				node.left = nNode
			else:
				node.right = nNode

			queue.append(nNode)

			isLeft = not isLeft
			if isLeft:
				index += 1

		return root


class Solution:
	def calcFullBinaryTreeNodeCount(self, root):
		if not root:
			return 0

		height = self.calcHeight(root)
		curNode, curLevel, count = root, 1, 0
		while curNode and curLevel < height:
			if self.findNoneChild(curNode.left, curLevel + 1, height):
				curNode = curNode.left
			else:
				curNode = curNode.right
				count += pow(2, height - curLevel - 1)

			curLevel += 1


		print('pow(2, height - 1) - 1:', pow(2, height - 1) - 1)
		print('count:', count)
		return pow(2, height - 1) - 1 + count

	def calcHeight(self, root):
		if not root:
			return 0

		leftHeight = self.calcHeight(root.left)
		rightHeight = self.calcHeight(root.right)

		return max(leftHeight, rightHeight) + 1

	def findNoneChild(self, root, curLevel, maxHeight):
		if not root:
			return True

		curNode = root
		while curNode and curLevel < maxHeight:
			if not curNode.left or not curNode.right:
				return True

			curNode = curNode.right
			curLevel += 1

		return False


if __name__ == '__main__':
	solution = Solution()
	root = TreeNode.genFullBinaryTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	count = solution.calcFullBinaryTreeNodeCount(root)
	print(count)




