# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], index]
            hashmap[num] = index

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n = n >> 1
        return res

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


a = Solution()
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))