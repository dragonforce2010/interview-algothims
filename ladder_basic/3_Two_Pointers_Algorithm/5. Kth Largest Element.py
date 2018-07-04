'''
Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

Challenge
O(n) time, O(1) extra memory.
'''
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    # def kthLargestElement(self, k, A):
    #     import heapq
    #     heapq.heapify(A)
    #     return heapq.nlargest(k, A)[-1]
        
        
    def kthLargestElement(self, k, A):
        import heapq
        heap = []
        for elem in A:
            heapq.heappush(heap, elem)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]

'''QuickSelect 方法
class Solution {
    /*
     * @param k : description of k
     * @param nums : array of nums
     * @return: description of return
     */
    public int kthLargestElement(int k, int[] nums) {
        // write your code here
        return quickSelect(nums, 0, nums.length - 1, k);
    }

    private int quickSelect(int[] nums, int left, int right, int k) {

        int pivot = nums[left];
        int i = left, j = right;
        while (i <= j) {
            while (i <= j && nums[i] > pivot) {
                i++;
            }
            while (i <= j && nums[j] < pivot) {
                j--;
            }
            if (i <= j) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i++;
                j--;
            }
        }

        if (left + k - 1 <= j) {
            return quickSelect(nums, left, j, k);
        }
        if (left + k - 1 >= i) {
            return quickSelect(nums, i, right, k - (i - left));
        }
        return nums[j + 1];
    }
}

'''