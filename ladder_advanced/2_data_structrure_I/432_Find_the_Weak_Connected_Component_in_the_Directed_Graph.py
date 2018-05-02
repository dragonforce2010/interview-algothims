'''Description
Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of its neighbors. (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct edge path.)

 Notice
Sort the element in the set in increasing order
Example
Given graph:

A----->B  C
 \     |  | 
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}
'''
"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def __init__(self):
        self.father = {}
    
    def find(self, label):
        if self.father[label] == label:
            return label
            
        self.father[label] = self.find(self.father[label])
        return self.father[label]
        
    def union(self, label1, label2):
        root1 = self.find(label1)
        root2 = self.find(label2)
        if root1 != root2:
            self.father[root2] = root1
    
    def connectedSet2(self, nodes):
        # write your code here
        if not nodes:
            return [[]]
            
        for node in nodes:
            self.father[node.label] = node.label
            
        for node in nodes:
            for nei in node.neighbors:
                self.union(node.label, nei.label)
                
        componentmap = {}
        for node in nodes:
            root = self.father[node.label]
            if root not in componentmap:
                componentmap[root] = [node.label]
            else:
                componentmap[root].append(node.label)
                
        return componentmap.values()
        
        
'''Summary
算法武器： 并查集 + 图
使用了3个for循环
- 第一个for用于初始化self.father并查集字典
- 第二个for用于将节点和其邻居节点进行合并
- 第三个for循环用于求解各个联通分量成员和其父节点的映射
'''