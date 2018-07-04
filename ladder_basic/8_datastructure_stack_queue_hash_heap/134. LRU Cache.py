'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''
class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    def __init__(self, capacity):
        if capacity <= 0:
            raise Exception("Invalid Parameter: Capacity value has to be grate than 0!")
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
        self.hash = {}
        
    # @return an integer
    def get(self, key):
        if key in self.hash:
            self.lru_adjust(key)
            return self.hash[key].next.value
        else:
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            self.hash[key].next.value = value
            self.lru_adjust(key)
        else:
            node = LinkedNode(key, value)
            self.push_back(node)
            
            if self.capacity < len(self.hash):
                self.pop_front()
    
    # Adjust linked list based on LRU policy
    # Recently accessed element is put in the tail of the linked list
    def lru_adjust(self, key):
        preNode = self.hash[key]
        if preNode.next is not self.tail:
            node = preNode.next
            preNode.next = node.next
            self.hash[node.next.key] = preNode
            self.push_back(node)
    
    # æ·»å åç´ å°é¾è¡¨çæ«å°¾
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None
    
    # å é¤é¾è¡¨ç¬¬ä¸ä¸ªåç´ 
    def pop_front(self):
        node = self.head.next
        self.head.next = node.next
        del self.hash[node.key]
        self.hash[node.next.key] = self.head
        
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
进行Set操作shi
###set、get操作以及lru更新时，我们都需要更新hash。

请参考有注释的代码：

class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        if capacity <= 0:
            raise Exception("Invalid Parameter: Capacity value has to be grate than 0!")
        # 创建一个链表的dummy node
        self.head = LinkedNode()
        # 创建链表的尾指针方便添加元素到尾部
        self.tail = self.head
        self.capacity = capacity
        # 使用hash表做key和ListNode前驱之间的映射，即通过key我可以找到这个ListNode节点的前驱，是前驱不是自己哦
        # 之所以使用前驱是因为我们在删除ListNode时我们需要使用到前驱元素，所以如果映射时就使用前驱，这样计算就方便
        self.hash = {}
        
    # @return an integer
    def get(self, key):
        # write your code here
        # 如果key在hash字典中，我们就查hash表得到其前驱，通过前驱的next指针拿到元素Node，然后返回其value
        # 每访问一次我们就要进行LRU策略调整，我们总是把最近访问的元素放到链表的尾部，表示最新
        if key in self.hash:
            self.lru_adjust(key)
            return self.hash[key].next.value
        else:
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.hash:
            # 如果找到，我们就更新节点值，同时进行LRU策略调整
            self.hash[key].next.value = value
            self.lru_adjust(key)
        else:
            # 如果没有找到我们就创建ListNode，然后将其插入到列表头部
            node = LinkedNode(key, value)
            self.push_back(node)
            
            # 如果超出空间了，我们就把最老元素删除，最老元素在头部
            if self.capacity < len(self.hash):
                self.pop_front()
    
    # Adjust linked list based on LRU policy
    # Recently accessed element is put in the tail of the linked list
    def lru_adjust(self, key):
        preNode = self.hash[key]
        if preNode.next is not self.tail:
            # Remove the node from lined list and push it back to the tail of the linked list
            # 根据给定最近被访问的key值，找到其节点，将其删除，然后再添加到链表尾部，表示最新最近被访问
            node = preNode.next
            preNode.next = node.next
            # 删除之后要跟新删除节点的key做对应的前驱节点
            self.hash[node.next.key] = preNode
            # 将最近被访问元素node放回到链表最尾部，表示最近最新
            self.push_back(node)
    
    # 添加元素到链表的末尾
    def push_back(self, node):
        # 在hash表中创建/跟新key值
        self.hash[node.key] = self.tail
        # 加入到链表尾部，让尾指针指向它
        self.tail.next = node
        # 尾指针后移
        self.tail = node
        # 最后一个元素的next指针置空
        node.next = None
    
    # 删除链表第一个元素
    def pop_front(self):
        # 获取删除node
        node = self.head.next
        # 删除
        self.head.next = node.next
        del self.hash[node.key]
        # 更新删除node后继节点的哈希表的值，更新其前驱
        self.hash[node.next.key] = self.head
'''