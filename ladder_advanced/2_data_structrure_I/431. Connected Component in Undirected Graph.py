'''Description
Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

 Notice
Each connected component should sort by label.
Clarification
Learn more about representation of graphs

Example
Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
'''
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    
    def connectedSet(self, nodes):
        # Write your code here
        self.v = {}
        for node in nodes:
            self.v[node.label] = False

        connComponentList = []
        for node in nodes:
            if not self.v[node.label]:
                connComponent = []
                self.dfs(node, connComponent)
                connComponentList.append(sorted(connComponent))
        return connComponentList
    
    def dfs(self, node, connComponent):
        self.v[node.label] = True
        connComponent.append(node.label)
        for neighbor in node.neighbors:
            if not self.v[neighbor.label]:
                self.dfs(neighbor, connComponent)
'''Summary
算法武器：深度优先搜索 + 访问字典（标记一个点是否被访问过）

本题也可以使用并查集进行求解

class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph

    # nodes是图中顶点集合        
    def connectedSet(self, nodes):
        # Write your code here
        # 标记顶点是否被访问过的哈希字典,key为node.label
        self.v = {}
        # 初始化self.v为False
        for node in nodes:
            self.v[node.label] = False

        # 定义联通组件列表，这是我们要求的答案
        connComponentList = []
        for node in nodes:
            # 如果该顶点没有被处理过
            if not self.v[node.label]:
                # 局部变量，联通组件
                connComponent = []
                # 从当前顶点node开始，深度优先搜索，将探索到的点加入联通组件中
                self.dfs(node, connComponent)
                # 探索结束后，将该联通组件加入到全局联通组件列表中
                connComponentList.append(sorted(connComponent))
        return connComponentList

    # 从当前顶点node开始，深度优先搜索，将探索到的点加入联通组件中        
    def dfs(self, node, connComponent):
        # 访问当前顶点，并将其加入局部联通组件中
        self.v[node.label] = True
        connComponent.append(node.label)
        # 访问邻居节点，继续进行深度优先搜索
        for neighbor in node.neighbors:
            # 如果处理过了就跳过
            if not self.v[neighbor.label]:
                self.dfs(neighbor, connComponent)
'''