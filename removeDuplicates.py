# -*- coding: utf-8 -*-
class Solution:
    # 元素重复时删除重复元素的同时将数组长度减1并且将指针前移一位
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                n -= 1
                i -= 1
            i += 1
        return nums
