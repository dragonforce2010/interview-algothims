'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]
'''
class Solution:
    def combinationSum2(self, candidates, target):
        self.result = []
        self.dfs(sorted(candidates), target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, valuelist):
        if target == 0:
            self.result.append(valuelist[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if target < candidates[i]:
                return

            valuelist.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i + 1, valuelist)
            valuelist.pop()
'''
算法武器：排序（帮助我们去重）+深度优先搜索+递归

dfs实质：在当前状态下，有多种选择，dfs会尝试各种选择，并且在选择之后，继续进行递归调用dfs，即沿着那个方向一直深度搜索下去，每种选择完毕之后，即dfs递归函数返回之后，我们需要恢复现场，取消当前的选择的影响，然后尝试下一个选择。由于是递归调用，所以现场恢复的事情递归自己就可以完成了，我们只需要把递归过程中操作/修改过的局部变量进行恢复就可以。

简而言之，dfs就是找出当前状态下的所有选择，用for循环处理每种选择，对于每种选择，处理一下，然后递归调用一下，递归结束时在将递归局部变量恢复，为了不影响下一次选择。

对比一下：bfs是依靠队列实现的，没有使用递归调用，二dfs大多数情况下都是使用递归完成的，一般不要自己模拟栈去实现递归，因为太麻烦。
记住：dfs是递归，bfs是非递归，用队列。

本题可以联想到2sum，3sum，4sum等问题，本题要求解出任意sum等于给定target的集合，这样我们只能以搜索的方式穷举所有的可能组合，然后将符合条件的解筛选出来放入集合之中。

在穷举所有解的时候我们需要考虑去重，为了有效的去重，我们需要对原序列进行排序，这样重复的元素会挨在一起，方便我们的去重操作。

声明一个全局变量，用于收集结果。
dfs是一个递归调用的函数，会以深度优先的方式，在每个节点进行（我们可以把本题画成一个庞大的搜索树），每个节点都会对递归结束条件判断，如果符合，就会将局部解加入到全局解之中。

注意：

	# 注意这里的下标我们传的是i + 1，而不是i，这保证了我们的元素不可以重复利用
	self.dfs(candidates, target - candidates[i], i + 1, valuelist)
这道题跟之前那道 Combination Sum 组合之和 本质没有区别，只需要改动一点点即可，之前那道题给定数组中的数字可以重复使用，而这道题不能重复使用，只需要在之前的基础上修改两个地方即可，首先在递归的for循环里加上if (i > start && num[i] == num[i - 1]) continue; 这样可以防止res中出现重复项，然后就在递归调用combinationSum2DFS里面的参数换成i+1，这样就不会重复使用数组中的数字了

def combinationSum2(self, candidates, target):
        # write your code here
        
        # 排序很重要，否则我们会漏掉结果
        self.result = []
        self.dfs(sorted(candidates), target, 0, [])
        return self.result
    
    # 以深度优先搜索的方式，从start位置开始探索candidates数组，探索所有的可能性，尝试加入candidates【i】到valuelist中或者不加，如果目标结果只为0，那么证明我们找到了有效的答案，我们将其加入总答案
    # valuelist是用来保存局部答案的局部变量，攻递归函数使用
    def dfs(self, candidates, target, start, valuelist):
        if target == 0: # 当target==0，证明这是一个有效的答案
            self.result.append(valuelist[:])
            return
        # 从当前index开始到结束，一次探测每个元素是否能够放在值列表之中    
        # 注意这里的i是从start开始的，我们在递归的下标是没有+1的，也就是说我们可以使用当前的元素任意多次
        for i in range(start, len(candidates)):
            # 如果target已经小与当前元素了，则后面的就不用探测了，因为没法再做加法了
            # 注意：这里是i > start
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if target < candidates[i]:
                return
            #加入局部值域列表
            valuelist.append(candidates[i])
            # 深搜
            # 注意这里的下标我们传的是i + 1，而不是i，这保证了我们的元素不可以重复利用
            self.dfs(candidates, target - candidates[i], i + 1, valuelist)
            # 回溯
            valuelist.pop()
'''