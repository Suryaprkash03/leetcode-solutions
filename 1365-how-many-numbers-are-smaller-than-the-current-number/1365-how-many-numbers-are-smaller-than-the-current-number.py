class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        mp = {}

        for i, num in enumerate(sorted_num):
            if num not in mp:
                mp[num] = i
        
        return [mp[num] for num in nums ]
        