from collections import defaultdict
import heapq 

class Solution:
    def encode(self, s):
        pass

    def get_freq_map(self, s):
        if not s:
            return {}

        myhash = defaultdict(int)
        for c in s:
            myhash[c] += 1

        return myhash

    def to_heap(self, myhash):
        if not myhash:
            return []

        heap = []
        for key, value in myhash.items():
            heapq.heappush(heap, (value, key))

        return heap

    def get_encoding_map(self, root):
        if not root:
            return {}

        encoding_map = {}
        encode_str = []
        self.dfs(root, encoding_map, encode_str)
        return encoding_map

    def dfs(self, root, result_map, local_str):
        if not root.left and not root.right:
            result_map[root.c] = ''.join(local_str)

        if root.left:
            local_str.append('0')
            self.dfs(root.left, result_map, local_str)
            local_str.pop()

        if root.right:
            local_str.append('1')
            self.dfs(root.right, result_map, local_str)
            local_str.pop()

    def encode_str_by_coding_map(self, encoding_map, str):
        if not str or not encoding_map:
            return str

        encoded = []
        for c in str:
            code = encoding_map.get(c)
            encoded.append(code)

        return ''.join(encoded)
    



class TreeNode:
    def __init__(self, c=None, freq=None, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.c  = c


    
    @classmethod
    def construct_from_freq_heap(cls, heap):
        if not heap:
            return None

        nodes = []
        while heap:
            freq, c = heapq.heappop(heap)
            node = TreeNode(c=c, freq=freq)
            nodes.append(node)

        # root1 = TreeNode(left=nodes[0], right=nodes[1], freq = nodes[0].freq + nodes[1].freq)
        # root2 = TreeNode(left=nodes[2], right=root1, freq=nodes[2].freq + root1.freq)

        root = nodes[0]
        for index in range(1, len(nodes)):
            node = nodes[index]
            root = TreeNode(right=root, left=node, freq=root.freq + node.freq)

        return root

    @classmethod
    def traverse(cls, root):
        if not root:
            return

        if root.left:
            TreeNode.traverse(root.left)

        print(root.c, root.freq)

        if root.right:
            TreeNode.traverse(root.right)
            
solution = Solution()
encode_string = 'CCCCCCCMMMM'
myhash = solution.get_freq_map(encode_string)

heap = solution.to_heap(myhash)

# while heap:
#     ele = heapq.heappop(heap)
#     print(ele)

tree = TreeNode.construct_from_freq_heap(heap)
# tree.traverse(tree)
encoding_map = solution.get_encoding_map(tree)
print(encoding_map)

print(solution.encode_str_by_coding_map(encoding_map, 'CCCCCCCMMMM'))



# encode_string2 = 'cccccccccccccccc'
# myhash2 = solution.get_freq_map(encode_string2)

# heap2 = solution.to_heap(myhash2)

# while heap:
#     ele = heapq.heappop(heap)
#     print(ele)

# tree2 = TreeNode.construct_from_freq_heap(heap2)
# TreeNode.traverse(tree2)



# print(myhash)