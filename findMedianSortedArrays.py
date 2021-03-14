class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 0:
            return (nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2
        else:
            return nums[int((len(nums)/2))]

nums1 = [1, 3]
nums2 = [2, 4]
a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))