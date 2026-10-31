class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0 

        for i in accounts:
            maxx = sum(i)
            max_wealth = max(max_wealth, maxx)
        return max_wealth