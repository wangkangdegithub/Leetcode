"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x = ['[', '(', '{']  # 左括号
        y = ["]", ")", "}"]  # 右括号
        z = ["()", "[]", "{}"]
        res = []

        if not s:
            return True
        for i in s:
            if i in x:
                res.append(i)  # 入栈
            elif i in y:  # 接收右括号
                if res == []:  # 如果res中无左括号，返回False
                    return False
                else:
                    temp = res.pop(-1) + i  # pop(-1)取出最右的项，同时把res的最后一项删除。temp=(左括号，右括号)
                    if temp not in z:
                        return False
        # 如果所有括号对都满足，但是res还有左括号，返回False
        if len(res) != 0:
            return False
        return True


if __name__ == '__main__':
    test = '([{}[]])()'
    b = Solution()
    print(b.isValid(s=test))
