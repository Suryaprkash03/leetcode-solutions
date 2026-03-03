class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            wealth = sum(account)
            max_wealth = max(max_wealth, wealth)
        return max_wealth
        