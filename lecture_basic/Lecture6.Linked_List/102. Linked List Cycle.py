'''
Given a linked list, determine if it has a cycle in it.



Example
Given -21->10->4->5, tail connects to node index 1, return true

Challenge
Follow up:
Can you solve it without using extra space?
'''
class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        # 注意：这里的slow和fast指针初始化时是不一样的
        # 因为后面的while的条件是当slow != fast, 所以我们不能把slow和fast初始化成相同的值
        # 反正只要快慢指针存在，并且有环，那么快指针一定会和慢指针重合即slow == fast
        slow, fast = head, head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True