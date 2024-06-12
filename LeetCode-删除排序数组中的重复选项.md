## 删除排序数组中的重复选项（点击查看原题：[remove-duplicates-from-sorted-array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)）
> 这个题给我的第一感觉，排序的数组，这下难度降低了许多，我最初想的是把不重复的数据都移到数组的前几位，这样也确实对的，能得到去除重复元素后数组的长度，但是这样本质上数组的长度还是和以前一样的。然后我又想到了移除元素这道题的做法，可以倒叙遍历数组，然后把数据移除，这样得到的数组也是移除重复数据的数组啦。  

代码如下：
```python
from typing import List


class Solution:
    # 方法一
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     nums_len = len(nums)
    #     for j in range(1, nums_len):
    #         if nums[i] != nums[j]:
    #             i += 1
    #             nums[i] = nums[j]
    #     print(nums) # 数组的长度还和之前一样，只是数据调换了下位置
    #     return i+1
    # 方法二
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        i = nums_len - 1
        for j in range(nums_len - 2, -1, -1):
            if nums[i] == nums[j]:
                nums.pop(j)
            i -= 1
        # print(nums) # 数组长移除重复数据后的数组
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(s.removeDuplicates([1, 1, 2]))

```