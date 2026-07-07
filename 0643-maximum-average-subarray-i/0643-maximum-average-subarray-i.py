class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        currSum = 0
        maxSum = 0
        winStart = 0

        for i in range(k):
            currSum += nums[i]
        
        maxSum = currSum

        for winEnd in range(k, len(nums)):
            currSum += nums[winEnd] - nums[winStart]
            maxSum = max(currSum, maxSum)
            winStart += 1

        return maxSum / k