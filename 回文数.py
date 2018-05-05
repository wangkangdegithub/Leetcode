"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            for i in range(len(str(x))):
                if int(str(x)[i]) == int(str(x)[len(str(x)) - 1 - i]):
                    continue
                else:
                    return False

            return True


# 优化方法

class newSolution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = str(x)
        m = n[::-1]
        if n == m:
            return True
        else:
            return False


if __name__ == '__main__':
    a = -12121
    b = newSolution()
    print(b.isPalindrome(x=a))
