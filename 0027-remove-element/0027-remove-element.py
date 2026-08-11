class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[idx] = nums[j]
                idx += 1
        return idx
