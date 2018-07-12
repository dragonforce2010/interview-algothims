'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''
class LinkedNode:
    '''
    - 我们使用LinkedList数据结构，保存数据同时表示数据的新旧，新的数据在最右，旧的数据在最左
    - 为了加快查找，我们使用字典，所以我们node节点中有一个key属性
    - 利用key属性我们可以查找到该node的前驱节点，便于删除该节点
    '''
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise Exception("Invalid parameter: Capacity value can not be less than 0")

        # 使用dummyHead作为链表头， 一开始头尾都指向同一个节点
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
        self.cache = {}

    # 先查cache，如果有则返回，否则返回-1
    # 如果cache中有，那么要进行一下lru策略调整，将当前访问的节点放到末尾，因为末尾表示最近访问过
    def get(self, key):
        if key in self.cache:
            self.lruAdjust(key)
            return self.cache[key].next.value
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            self.cache[key].next.value = value
            self.lruAdjust(key)
        else:
            node = LinkedNode(key, value)
            self.append(node)

            if self.capacity < len(self.cache):
                self.popleft()

    # 凡是接受lruAdjust的元素都是已经存在于cache中的元素
    def lruAdjust(self, key):
        preNode = self.cache[key]
        # 如果要调整的元素就是链表最末尾的元素，那么我们就不用调整，因为已经是最新的了
        if preNode.next is not self.tail:
            node = preNode.next
            preNode.next = node.next
            self.cache[node.next.key] = preNode
            self.append(node)

    # 把一个节点加入到链表末尾
    def append(self, node):
        self.cache[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    # 把链表头的元素删除
    def popleft(self):
        node = self.head.next
        self.head.next = node.next
        del self.cache[node.key]
        self.cache[node.next.key] = self.head

'''
算法武器： hash + linkedlist

为了加快元素的插入和删除，我们使用链表这个数据结构来存储数据。为了加速元素的访问，我们使用hash表来记录元素的key值和其节点的映射关系。
因为元素的插入和删除我们都需要用到元素的前驱，所以我们在哈希表中的映射关系是元素key和其前驱节点的映射。

LRU的表示？如何表示一个元素是最近被访问过？

我们把最近访问的元素都放到链表的末尾，越靠近链表末尾代表最近被访问，越靠近链表头，代表数据被访问的频率越少
所以移除元素时我们总移链表的头部所指的下一个元素，加入元素时，我们总把元素加到末尾
LRU的更新策略时机：

进行Set操作时需要更新LRU策略
进行Get操作时需要更新LRU策略
'''