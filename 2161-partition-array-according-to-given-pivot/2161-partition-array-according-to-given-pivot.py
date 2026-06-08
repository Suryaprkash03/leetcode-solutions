class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ltp = []
        ep = []
        gtp = []

        for num in nums:
            if num < pivot:
                ltp.append(num)
            elif num == pivot:
                ep.append(num)
            else:
                gtp.append(num)
        return ltp + ep + gtp