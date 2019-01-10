#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    """
    852.山脉数组的峰顶索引
    我们把符合下列属性的数组 A 称作山脉：
    A.length >= 3
    存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
    """

    def peakIndexInMountainArray1(self, A):
        """
        :param A:List[int]
        :return: int
        """
        k = A[0]
        for i in range(1, len(A)):
            if A[i] < k:
                return i - 1
            else:
                k = A[i]
        return k

    def peakIndexInMountainArray(self, A):
        left, right = 0, len(A)
        while left < right:
            mid = int((left + right) / 2)
            if A[mid] < A[mid + 1]:  # 如果是大的话，目标一定是mid+1
                left = mid + 1
            else:
                right = mid
        return left

    pass


if __name__ == "__main__":
    s = Solution()
    A = [0, 2, 1, 0]
    print(s.peakIndexInMountainArray(A))
    pass
