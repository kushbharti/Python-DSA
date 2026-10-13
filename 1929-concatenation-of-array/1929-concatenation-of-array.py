class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        arr = []
        counter = 0
        for i in range( (len(nums)*2) +  1 ):
            if len(nums) < i:
                arr.append(nums[counter])
                counter += 1
            if len(nums) > i:
                arr.append(nums[i])
        return arr