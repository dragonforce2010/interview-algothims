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
class Solution:
    def __init__(self):
        self.father = {}
        
    def find(self, x):
        if self.father[x] == x:
            return x
            
        self.father[x] = self.find(self.father[x])
        return self.father[x]
        
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.father[rooty] = rootx
            
    def connectedSet2(self, nodes):
        for node in nodes:
            self.father[node.label] = node.label
            
        for node in nodes:
            for nei in node.neighbors:
                self.union(node.label, nei.label)
                
        compMapping = {}
        for node in nodes:
            father = self.find(node.label)
            if father not in compMapping:
                compMapping[father] = [node.label]
            else:
                compMapping[father].append(node.label)
                
        return compMapping.values()
'''Summary
算法武器： 并查集 + 图

使用了3个for循环
- 第一个for用于初始化self.father并查集字典
- 第二个for用于将节点和其邻居节点进行合并
- 第三个for循环用于求解各个联通分量成员和其父节点的映射
'''