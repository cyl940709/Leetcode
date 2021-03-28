# -*- coding: utf-8 -*-
from typing import List
class Solution:
    # 将grid的第一行和第一列逐行（列）相加， 之后的数取上或左较小的数与其本身相加填入grid，最后返回grid最后一个数字
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
    # dp数组代表对应的字符子串所能构成的不同编码，需要注意的是0这个点，遇到0时需要把dp值回退到上上个点
    # 通过and和or可以省略很多行代码
    def numDecodings(self, s: str) -> int:
        s, dp = list(s), [0] * len(s)
        if s[0] == "0": return 0
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i - 1] != "1" and s[i - 1] != "2": return 0
                dp[i] = dp[i - 2] if i >= 2 else 1
            elif s[i - 1] == "1" or s[i - 1] == "2" and s[i] <= "6":
                dp[i] = dp[i - 1] + dp[i - 2] if i >= 2 else dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

    # dp[i][j]代表的是以此点为右下角的正方形的最大边长
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        # r为矩阵的行，c为矩阵的列
        r, c = len(matrix), len(matrix[0])
        # dp矩阵初始化
        dp = [[0] * c for _ in range(r)]
        for i in range(c): dp[0][i] = int(matrix[0][i])
        for i in range(r): dp[i][0] = int(matrix[i][0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        maxNums = []
        for i in range(len(dp)):
            maxNums.append(max(dp[i]))
        maxSide = max(maxNums)
        return maxSide*maxSide
    # 任务完成所需要的最短时间取决于任务列表中出现次数最多的任务
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        return res if res > len(tasks) else len(tasks)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        text1 = list(text1)
        text2 = list(text2)
        a = len(text1) + 1
        b = len(text2) + 1
        dp = [[0] * a for _ in range(b)]
        for i in range(1, b):
            for j in range(1, a):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1 if text1[j-1] == text2[i-1] else max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    pass
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + 1
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = min(
                        [dp[i][j - 1] + 1, dp[i - 1][j] + 1,
                         dp[i - 1][j - 1] + int(word1[i - 1] != word2[j - 1])])
        return dp[-1][-1]

