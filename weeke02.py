# -*- coding: utf-8 -*-
from typing import List
import itertools

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]

    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5: return False
        package = []
        try:
            for i in bills:
                if i == 5:
                    package.append(i)
                elif i == 10:
                    package.remove(5)
                    package.append(10)
                else:
                    if 10 in package:
                        package.remove(10)
                        package.remove(5)
                        package.append(20)
                    else:
                        package.remove(5)
                        package.remove(5)
                        package.remove(5)
                        package.append(20)
        except:
            return False
        return True

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                temp = prices[i+1] - prices[i]
                profit += temp
        return profit

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in range(len(s)):
            if s[i] >= g[count]:
                count += 1
                if count == len(g):
                    break
        return count

    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrack(nums, [])
        res1 = []
        for i in res:
            if i not in res1:
                res1.append(i)
        return res1

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return 0
        elif n < 0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n = n >> 1
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        def backtrack(i, tmp):
            res.append(tmp)
            for j in range(i, len(nums)):
                backtrack(j + 1, tmp + [nums[j]])
        backtrack(i, [])
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(condition, nextdigit):
            if len(nextdigit) == 0:
                res.append(condition)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(condition + letter, nextdigit[1:])

        res = []
        condition = ''
        backtrack(condition, digits)
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        landNums = 0
        if len(grid[0]) == 0:
            return 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    landNums += 1
                    self.dfs(grid, y, x)
        return landNums

    def dfs(self, grid, y, x):
        grid[y][x] = 0
        ny, nx = len(grid), len(grid[0])
        for i, j in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if 0 <= i < ny and 0 <= j < nx and grid[i][j] == "1":
                self.dfs(grid, i, j)

    def canJump(self, nums: List[int]) -> bool:
        rightmost = 0
        for i in range(len(nums)):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= len(nums) - 1:
                    return True
        return False

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        s = "." * n

        def backtrack(i, tmp, col, z_diagonal, f_diagonal):
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and i + j not in z_diagonal and i - j not in f_diagonal:
                    backtrack(i + 1, tmp + [s[:j] + "Q" + s[j + 1:]], col | {j}, z_diagonal | {i + j},
                              f_diagonal | {i - j})

        backtrack(0, [], set(), set(), set())
        return res

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step