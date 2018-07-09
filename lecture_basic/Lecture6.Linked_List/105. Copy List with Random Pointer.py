'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Challenge
Could you solve it with O(1) space?
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        cache = {}
        # 创建新链表头的克隆
        nHead = RandomListNode(head.label)
        cache[head] = nHead
        cur1, cur2 = head, nHead

        # 扫面旧链表，只拷贝普通节点，不考虑random的拷贝，在新链表中，依然将random指向老链表的节点
        # 在不断拷贝过程中，把新老节点的映射关系放到cache中，以便查找
        while cur1:
            # 新链表中依旧使用老链表的random节点
            cur2.random = cur1.random
            # 拷贝next指向节点
            if cur1.next:
                cur2.next = RandomListNode(cur1.next.label)
                cache[cur1.next] = cur2.next
            else:
                cur2.next = None

            # 移动游标
            cur1 = cur1.next
            cur2 = cur2.next

        # 扫描新链表，处理random指针
        cur = nHead
        while cur:
            if cur.random:
                cur.random = cache[cur.random]
            cur = cur.next

        return nHead

'''
算法武器：链表 + 哈希表 + 双游标指针 + 分阶段两次扫描

算法思路：

首先定义一个哈希表，使用该哈希表记录原有节点和克隆节点的映射，因为稍后我们需要根据原节点，查询到克隆节点
克隆链表的头节点，并将其加入哈希表和老节点进行映射
定义双游标指针，分别指向新老链表
使用while循环处理节点克隆，结束条件为老链表还没有走到末尾
对于每一个遍历到的老节点，我们需要做两件事：
处理随机指针，因为本次克隆我们在我们构建完新链表之前无法做到对新链表的随机指针的克隆，因为新链表的随机指针可能指向新链表的后面的节点，但是这些节点还没有被克隆出来，所以我们本次while循环对随机指针的处理是让其依然指向老节点，随后通过查表获得新节点引用
处理next指针的克隆，处理之前判断是否有next指针，有就克隆，同时建立映射，没有就将其赋值为空
移动新老节点的游标指针，进行下一个节点的处理
第一趟基本克隆结束之后，我们再对新链表进行一次扫面，专门处理随机指针，将之前指向老节点的随之指针通过查表指向新节点

'''