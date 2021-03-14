# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], index]
            hashmap[num] = index