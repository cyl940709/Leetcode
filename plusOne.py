# -*- coding: utf-8 -*-
class Solution:
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