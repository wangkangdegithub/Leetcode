"""

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]


# 优化方法
class newSolution(object):
    def twoSum(self, nums, target):
        """ 
        :type nums: List[int] 
        :type target: int 
        :rtype: List[int] 
        """
        arr = {}  # 使用字典存储遍历过的num和对应下标{num:index}
        length = len(nums)  # 计算输入的列表长度
        for i in range(length):
            if (target - nums[i]) in arr:  # 如果target-当前num的差在arr中，则表示已经找到答案，返回结果即可
                return [arr[target - nums[i]], i]
            arr[nums[i]] = i  # 否则，将该num及其下标存入arr中


if __name__ == "__main__":
    list = [5, 6, 7, 5]
    target = 10
    x = Solution()
    result = x.twoSum(nums=list, target=target)
    print(result)
