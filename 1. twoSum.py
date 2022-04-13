class Solution(object):
    def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     #n^2

    #Method 1:
    #     ls = len(nums)
    #     for i in range(ls):
    #         #print(i)
    #         for j in range(i + 1, ls):
    #             print(j)
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # Method 2:
    # def twoSum(self, nums, target):
    #     # hash 1
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         try:
    #             hash_nums[num].append(index)
    #         except KeyError:
    #             hash_nums[num] = [index]
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             candicate = hash_nums[another]
    #             if another == num:
    #                 if len(candicate) > 1:
    #                     return candicate
    #                 else:
    #                     continue
    #             else:
    #                 return [index, candicate[0]]
    #         except KeyError:
    #             pass

    # Method 3:
    # def twoSum(self, nums, target):
    #     # hash 2
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             hash_nums[another]
    #             return [hash_nums[another], index]
    #         except KeyError:
    #             hash_nums[num] = index

    # Method 4:
    # def twoSum(self, nums, target):
    #     # two point
    #     nums_index = [(v, index) for index, v in enumerate(nums)]
    #     nums_index.sort()
    #     begin, end = 0, len(nums) - 1
    #     while begin < end:
    #         curr = nums_index[begin][0] + nums_index[end][0]
    #         if curr == target:
    #             return [nums_index[begin][1], nums_index[end][1]]
    #         elif curr < target:
    #             begin += 1
    #         else:
    #             end -= 1

# Given an array of integers,return indices of the two numbers such that they add upto a specific target
# You may assume that each input would have exactly one solution
#
# Maintain a mapping from each number to its index
# Check if target - num has already been found
# Time - O(n)
# Space - O(n) for the dictionary

    # Method 5:
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i
        return

if __name__ == '__main__':
    # begin
    s = Solution()
    print (s.twoSum([3, 2, 4], 7))
