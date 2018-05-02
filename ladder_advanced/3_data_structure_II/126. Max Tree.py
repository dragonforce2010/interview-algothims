'''Description
Given an integer array with no duplicates. A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        if not A:
            return None 
            
        stack = []
        # scan the array A
        for ele in A:
            # contruct the tree node for current ele
            node = TreeNode(ele)
            while stack and ele > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            # push current node to stack
            stack.append(node)
        return stack[0]


'''Summary
http://www.jianshu.com/p/e05e598c8073
LintCode 126 [Max Tree]
144 作者 Jason_Yuan 关注
2015.09.27 11:46* 字数 403 阅读 447评论 0喜欢 0
原题

给出一个没有重复的整数数组，在此数组上建立最大树的定义如下：
1.根是数组中最大的数
2.左子树和右子树元素分别是被父节点元素切分开的子数组中的最大值
利用给定的数组构造最大树。
给出数组 [2, 5, 6, 0, 3, 1]，构造的最大树如下：

     6
    / \
   5   3
  /   / \
 2   0   1
解题思路

通过观察发现规律，对于每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的)
维护一个降序数组，可以实现对这个min的快速查找

stack = [2], push 5 因为 5 > 2, 所以2是5的左儿子, pop 2
stack = [], push 5
stack = [5], push 6, 因为 6 > 5，所以5是6的左儿子, pop 5
stack = [], push 6
stack = [6], push 0, 因为0 < 6, stack = [6], 所以0是6的右儿子
stack = [6, 0], push 3, 因为3 > 0, 所以0是3的左儿子， pop 0
stack = [6], 所以3是6的右儿子， push 3
stack = [6, 3], push 1, 因为1 < 3，所以1是3的右儿子
完整代码

"""
Definition of TreeNode:
class TreeNode:
def init(self, val):
self.val = val
self.left, self.right = None, None
"""
class Solution:
# @param A: Given an integer array with no duplicates.
# @return: The root of max tree.
def maxTree(self, A):
# write your code here
stack = []
for element in A:
node = TreeNode(element)
while len(stack) != 0 and element > stack[-1].val:
node.left = stack.pop()
if len(stack) != 0:
stack[-1].right = node
stack.append(node)
return stack[0]

这是lintcode上的一题，每次先确定根结点最大值，然后根据根结点再分割左右两边，然后继续。按照描述是一个递归过程。但是直接用递归是O(nlogn)的平均复杂度，最坏复杂度为O(n^2),即为有序数组时，但是这题用递归解法在Lintcode上直接爆栈。

所以需要时间和空间复杂度都为O(n)的解法，仔细分析下这题，给出的数组实际是max-tree的一个中序遍历。max-tree有一个特点，每个节点的祖先节点都比其值大．并且一个父亲节点的两个孩子节点在中序遍历中无法紧邻（必须经过父亲节点）所以一个节点左边和右边第一个比它大的都是它的祖先节点．左右比它小的实际是它的孩子子树遍历的结果．

每个结点的父结点都比结点值要大，并且结合中序遍历的性质，如果结点为父结点的左孩子，则在数组中是［结点...父结点］这样的顺序，而如果是右结点，则在数组中是［父结点...结点]这样的顺序。而省略号代表的是结点自己的右子树序列（结点为父结点的左孩子的情况），结点自己的左子树序列（结点为父结点的左孩子的情况），所以...的内容中都是比结点值小的。所以结点的父结点是其左边或者右边第一个比它大的值。在结点是父结点的左右孩子的情况下，如何确定父亲结点是哪个呢。按照推理我们选择其中比较小的那个。因为左右第一个比它大的值都是它的祖先节点．如果我们选择比较大的那个．则另外一个比较小的节点也是这个节点的祖先节点，爷爷节点及以上，所以这个比较小的节点最终成了这个比较大的节点的祖先节点．显然不符合max-tree的特性．

以上得出结论：每个节点的父亲节点，是其左边和右边第一个比它大的数的中的比较小的那个．显然数据结构是使用单调递减栈，时间和空间复杂度都是O(n)
'''