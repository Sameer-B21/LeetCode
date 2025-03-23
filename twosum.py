class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}

        for n in range(len(nums)):
            temp = target - nums[n]
            if temp in h:
                return [n, h[temp]]
            h[nums[n]] == n
       