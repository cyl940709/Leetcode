# -*- coding: utf-8 -*-

class Solution:
    # 双指针，非0元素j指针才加1，然后将对应的非零元素覆盖到原值上去，否则不动，i指针由于在有0的情况下跑得比j指针快，自然而然将后边的值都赋值成了0
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1
        return nums

    # 将非零元素和零元素分隔开存放到不同数组中，最后合并数组
    def moveZeroes2(self, nums):
        nonzeroList = []
        zeroList = []
        for i in nums:
            if i != 0:
                nonzeroList.append(i)
            else:
                zeroList.append(i)
        for i in zeroList:
            nonzeroList.append(i)
        return nonzeroList

    # 遇到0则最后添加一个0，然后删掉一个0 时间复杂度有点儿高O(n²)
    def moveZeroes3(self, nums):
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(0)
        return nums