'''
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?
'''
# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    '''
    DFS algorithm
    '''
    def topSort(self, graph):
        if not graph:
            return []
            
        degrees = {}
        for node in graph:
            degrees[node] = 0
            
        for node in graph:
            for nei in node.neighbors:
                degrees[nei] += 1
        
                
        result = []
        for node in graph:
            if degrees[node] == 0:
                self.dfs(degrees, node, result)
                
        return result
        
        
    def dfs(self, degrees, node, result):
        result.append(node)
        
        if not node.neighbors:
            return 
        
        '''
        1.这一步非常关键，因为我们已经输出了node，因为它的度是0，我们不希望这个node被重新输出，因为这个node可能会被主函数里的for循环输出，所以这里我们要再把这个node的度减1使其变成-1，以避免多次输出
        2.注意，dfs会对度进行更新，这影响for循环。我们初始的for循环指向从初始的度为0的点开始递归调用，这些点可能有3个，但是dfs的更新会使点增多，变成5个，10个，这样for循环就重复处理了dfs中已经处理过的度为0的点，所以我们使用上面的步骤避免重复
        '''
        degrees[node] -= 1
        for nei in node.neighbors:
            degrees[nei] -= 1
            if degrees[nei] == 0:
                self.dfs(degrees, nei, result)
                
                
                
    
    
    '''
    BFS algorithm
    '''
    def topSort2(self, graph):
        # write your code here
        if not graph:
            return []
            
        '''初始化度数组'''    
        degrees = {}
        for node in graph:
            degrees[node] = 0
            
        '''根据图的边信息，计算更新度书组'''
        for node in graph:
            for nei in node.neighbors:
                degrees[nei] += 1
                
                
        '''初始化队列，将入度为0的节点加入到队列中'''
        from collections import deque
        queue = deque([])
        for node, degree in degrees.items():
            if degree == 0:
                queue.append(node)
            
        result = []    
        '''
        1.循环遍历队列中的元素
        2.出队，将元素加入到结果集
        3.更新度数组，将度为0的点加入队列
        '''
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in node.neighbors:
                degrees[nei] -= 1
                if degrees[nei] == 0:
                    queue.append(nei)
                    
        return result
