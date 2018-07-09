'''
Reverse a linked list.

Example
For linked list 1->2->3, the reversed linked list is 3->2->1

Challenge
Reverse it in-place and in one-pass
'''
class Solution:
    def reverse(self, head):
        prev, curr, next = None, head, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

'''
算法武器：链表 + 三个游标指针(prev, curr, next)

算法思路：

定义三个指针进行翻转操作（prev, curr, next）
使用一个while循环进行列表翻转
while的循环条件为curr不为空
while退出后，prev指向翻转后的列表的头结点
翻转4部曲

保存next指针
当前指针后继指向前驱
前驱向后移动，指向当前
当前向后移动，指向next
'''