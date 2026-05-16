class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hash_map:
                return [hash_map[comp], i]
            hash_map[num] = i