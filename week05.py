# -*- coding: utf-8 -*-
from collections import Counter
from typing import List

class Solution:
    # 判断图形是否为正方形
    def distance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def isRectangle(self, points) -> bool:
        lines = []
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                lines.append(self.distance(points[i], points[j]))
        lines = list(set(lines))
        if len(lines) == 1:
            return False
        elif len(lines) == 2:
            if min(lines) * 2 == max(lines):
                return True
            else:
                return False
        elif len(lines) == 3:
            lines.sort()
            if lines[0] + lines[1] == lines[2]:
                return True
            else:
                return False
        else:
            return False
    # 数组的相对排序
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = 0
        p = 0
        n, m = len(arr1), len(arr2)
        while i < m:
            tmp = arr2[i]
            for j in range(n):
                if arr1[j] == tmp:
                    arr1[p], arr1[j] = arr1[j], arr1[p]
                    p += 1
            i += 1
        for j in range(p, n - 1):
            for k in range(j + 1, n):
                if arr1[k] < arr1[j]:
                    arr1[k], arr1[j] = arr1[j], arr1[k]
        return arr1

    # 有效的字母异位词
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = "".join((lambda x: (x.sort(), x)[1])(list(s)))
        s2 = "".join((lambda x: (x.sort(), x)[1])(list(t)))
        return True if s1 == s2 else False
    # 字符串中的第一个唯一字符
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for key, value in c.items():
            if value == 1:
                return s.index(key)
        return -1
    # 验证回文字符串 Ⅱ
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s): return True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isPalindrome(s[left+1 : right+1]) or self.isPalindrome(s[left:right])
        return True
# LRU缓存机制
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到末尾，所以定义一个方法
    def move_node_to_tail(self, key):
            # 先将哈希表key指向的节点拎出来，为了简洁起名node
            #      hashmap[key]                               hashmap[key]
            #           |                                          |
            #           V              -->                         V
            # prev <-> node <-> next         pre <-> next   ...   node
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            # 之后将node插入到尾节点前
            #                 hashmap[key]                 hashmap[key]
            #                      |                            |
            #                      V        -->                 V
            # prev <-> tail  ...  node                prev <-> node <-> tail
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
