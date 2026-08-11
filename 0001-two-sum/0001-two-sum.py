class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            needed = target - num
            # is present or not.
            if needed in seen:
                return [seen[needed],i]
            seen[num] = i
        return []

