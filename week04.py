# -*- coding: utf-8 -*-
from typing import List
import math
from collections import  deque

class Solution:
    # 爬楼梯
    def climbStairs(self, n: int) -> int:
        res = pow((1 + math.sqrt(5)) / 2, n + 1) - pow((1 - math.sqrt(5)) / 2, n + 1)
        return int(res / math.sqrt(5))
    # 岛屿数量
    def numIslands(self, grid):
        def dfs(grid, y, x):
            grid[y][x] = 0
            ny, nx = len(grid), len(grid[0])
            for i, j in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                if 0 <= i < ny and 0 <= j < nx and grid[i][j] == "1":
                    dfs(grid, i, j)

        landNums = 0
        if len(grid[0]) == 0:
            return 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    landNums += 1
                    dfs(grid, y, x)
        return landNums
    # 位1的个数
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n&1
            n >>= 1
        return res
    # 单词接龙
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = deque([beginWord])
        res = 1
        visited = set()
        visited.add(beginWord)
        wordList = set(wordList)
        while d:
            size = len(d)
            for k in range(size):
                word = d.popleft()
                wordL = list(word)
                for i in range(len(wordL)):
                    for j in range(26):
                        tmp = wordL[i]
                        wordL[i] = chr(j + 97)
                        newWord = ''.join(wordL)
                        if newWord not in visited and newWord in wordList:
                            if newWord == endWord:
                                return res + 1
                            d.append(newWord)
                            visited.add(newWord)
                        wordL[i] = tmp
            res += 1
        return 0

    # N皇后1
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        dfs([], [], [])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            # 当board[i][j]访问完后，置其为‘’
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False
    # 兑换零钱
    # 贪心+dfs超时
    def dfs1(self, coins, i, amount, count):
        if amount == 0:
            self.ans = min(self.ans, count)
            return
        if i >= len(coins) or amount // coins[i] + count > self.ans: return
        for j in range(amount // coins[i], -1, -1):
            self.dfs(coins, i + 1, amount - coins[i] * j, count + j)

    def coinChange1(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.ans = float('inf')
        self.dfs(coins, 0, amount, 0)
        return self.ans if self.ans < float('inf') else -1

    # DP永远滴神
    # 完全背包问题
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [10001] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp

