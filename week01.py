# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], index]
            hashmap[num] = index
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
  def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k + 1
        self.deque = [0 for _ in range(self.capacity)]
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.deque[self.front] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.deque[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            return self.deque[self.front]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.deque[(self.rear - 1 + self.capacity) % self.capacity]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.front == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if (self.rear + 1) % self.capacity == self.front:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
    # 思路为将数组转成数字，然后转成字符串+1再转成数组
    def plusOne1(self, digits):
        l = len(digits)-1
        res = 0
        n = 0
        while l >= 0:
            res += digits[l] * pow(10, n)
            l -= 1
            n += 1
        return [int(x) for x in str(res+1)]
    # 分类讨论，如果末位为9以外的数字，直接末位加1，如果为9则一直进位到不是9的数，如果全都是9，则在首位插入1，其他位变0
    def plusOne2(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
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
