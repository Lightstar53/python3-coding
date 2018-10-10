class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]


def two_sum_map(nums, target):
    map = {}
    for i in range(0, len(nums)):
        compliment = target - nums[i]
        if map.get(compliment) is not None:
            return [map.get(compliment), i]
        map[nums[i]] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 7))

print(two_sum_map([3,2,4], 7))
print(two_sum_map([-1, 10, 7, 6, 3, 4, 7], 14))