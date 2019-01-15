#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    """
    973.最接近原点的K个点
    """

    def kClosest1(self, points, k):
        """
        :param points:List[List[int]]
        :param k: int
        :return: List[List[int]]
        """
        # 根据欧几里德距离排序
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]

    def kClosest(self, points, k):
        tmp_dict = {}
        tmp_list = []
        for point in points:
            tmp_dict[point[0] ** 2 + point[1] ** 2] = point
            tmp_list.append(point[0] ** 2 + point[1] ** 2)
        tmp_list.sort()
        newlist = []
        for i in range(k):
            newlist.append(tmp_dict[tmp_list[i]])
        print(newlist)


if __name__ == "__main__":
    s = Solution()
    """ 
    """
    points = [[1, 3], [-2, 2]]
    k = 2
    lst = s.kClosest(points, k)
    print(lst)
    pass
