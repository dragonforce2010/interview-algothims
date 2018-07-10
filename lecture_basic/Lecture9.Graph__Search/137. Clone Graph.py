'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/
Example
return a deep copied graph.
'''
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def __init__(self):
        self.cache = {}

    def cloneGraph(self, node):
        if node is None:
            return None

        if node in self.cache:
            return self.cache[node]

        root = UndirectedGraphNode(node.label)
        self.cache[node] = root

        for nei in node.neighbors:
            root.neighbors.append(self.cloneGraph(neighbor))

        return root
    
'''
算法武器：分治递归 + 字典

算法思想：

克隆一个图就是把给定的图顶点克隆，以及把其兄弟节点克隆
因为图中的兄弟节点会相互重复，为了防止重复克隆，我们使用字典保存克隆前和克隆后节点的映射关系，如果已经克隆了，我们就直接在字典中查找返回即可
'''
