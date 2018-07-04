'''
The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

size=3, capacity=4

[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
The hash function is:

int hashcode(int key, int capacity) {
    return key % capacity;
}
here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
Given the original hash table, return the new hash table after rehashing .

Example
Given [null, 21->9->null, 14->null, null],

return [null, 9->null, null, null, null, 21->null, 14->null, null]
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    
    def rehashing(self,hashTable):
        anshashTable = [None for i in range(len(hashTable) * 2)]
        HASH_SIZE = 2 * len(hashTable)
        for item in hashTable:
            p = item
            while p != None:
                self.addnode(anshashTable,p.val)
                p = p.next
        return anshashTable
        
        
    def addnode(self, anshashTable, number):
        p = number % len(anshashTable)
        if anshashTable[p] == None:
            anshashTable[p] = ListNode(number)
        else:
            self.addlistnode(anshashTable[p], number)    
            
            
    def addlistnode(self, node, number):
        if node.next != None:
            self.addlistnode(node.next, number)
        else:
            node.next = ListNode(number)

'''
算法武器：hash + list

注意：

在rehashing的时候，要注意我们使用的哈希函数为hashcode = val % hash_size， 这在python里面是没有问题的，因为取模运算在python中总是返回正数。在java中我们要用这个公式： a % b = (a % b + b) % b
我们在遍历源链表时取出每一hash表中的list节点的引用，我们要查看该引用是不是一个链表，如果由于冲突，在这个节点形成了冲突链，那么我们得把每个节点都遍历到，重新计算hashcode，并且放入新的hash表
在新的hash表中，当我们把一个元素放入到hash表中时，我们也得考虑到冲突
如果冲突已经发生，那么我们就把元素放到冲突链的末尾
'''