class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp not in hash_map:
                hash_map[num] = i
            else:
                return [hash_map[comp],i]
            