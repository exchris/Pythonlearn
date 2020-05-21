# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 506相对名次

class Solution:
    def findRelativeRanks(self, nums):
        """
        :param nums:
        :return:
        """

        # 数组排序后的结果
        """
        l = []
        nums.sort(reverse=True)
        for idx, num in enumerate(nums):
            if idx == 0:
                l.append("Gold Medal")
            elif idx == 1:
                l.append("Silver Medal")
            elif idx == 2:
                l.append("Bronze Medal")
            else:
                l.append(str(idx + 1))
        return l
        """

        # 原数组结果
        tmp = [x for x in nums]
        tmp.sort(reverse=True)
        dic = {}

        for r in range(0, len(tmp)):
            if r == 0:
                dic[tmp[r]] = "Gold Medal"
            elif r == 1:
                dic[tmp[r]] = "Silver Medal"
            elif r == 2:
                dic[tmp[r]] = "Bronze Medal"
            else:
                dic[tmp[r]] = str(r + 1)
        return [dic[x] for x in nums]


s = Solution()
t = s.findRelativeRanks([10, 3, 8, 9, 4])
print(t)
