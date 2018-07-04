'''
Partition an unsorted integer array into three parts:

The front part < low
The middle part >= low & <= high
The tail part > high
Return any of the possible solutions.

Example
Given [4,3,4,1,2,3,1,2], and low = 2 and high = 3.

Change to [1,1,2,3,2,3,4,4].

([1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not)

Challenge
Do it in place.
Do it in one pass (one loop).
'''
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} low an integer
    # @param {int} high an integer
    # @return nothing
    def partition2(self, nums, low, high):
        # Write your code here
        if len(nums) <= 1:
            return
        
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] < low:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] > high:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

'''
算法武器：三指针

备注：本题的三指针为区域指针，每个指针维护一定区域的元素

算法思路：

使用三个指针策略
left/right指针分别指向数组的最左和最右
i指针为游标指针，在left和right指针之间进行扫描
left指针指向数组元素小于low的元素，[0,left)总维护小于low的元素
right指针指向数组元素大于high的元素，(right, len - 1]维护大于high的元素
left和right指针之间维护介于low和high的元素
游标i指针在扫描过程中，如果发现元素大于hight，就把该元素和right指针指向元素交换，是的right总是指向大于high的元素，同时把right的指针移动位置right -= 1
如果发现元素在<=low和>=high之间，那么就把i指针向前移动一位，因为这是i管辖范围的元素
如果发现元素小于low，就把该元素和left指针所指元素交换，是的left总指向小于low的元素，然后将left和游标i指针都向前挪动一位。游标i之所以要先前移动一位是因为从left交换过来的元素一定是在low、high之间的，因为i走过的元素就一定是在low、high之间。如果i和left进行一次交换，换过的一定是i所管辖区域的元素，我们必须让i + 1，而且i必须是比left大的，如果在和left交换之后，i不向前移位的话，i就会小于left，while循环会不断判断nums[i],算法就完全错了，left会因为此而可能超出上届
注意while循环条件： i <= right
right指针所指的位置是下一个有可能值大于high的元素，right位置处尚未探测到，所以i必须得取到等于right值才能保证算法完整性。
'''