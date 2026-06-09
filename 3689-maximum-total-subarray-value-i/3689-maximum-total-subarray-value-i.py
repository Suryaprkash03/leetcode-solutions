class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mn = min(nums)
        return k * (mx - mn)