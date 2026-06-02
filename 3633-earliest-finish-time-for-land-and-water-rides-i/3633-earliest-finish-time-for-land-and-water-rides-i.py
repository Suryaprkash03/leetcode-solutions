class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                land_finish = landStartTime[i] + landDuration[i]
                water_finish = max(land_finish, waterStartTime[j]) + waterDuration[j]

                water_finish_first = waterStartTime[j] + waterDuration[j]
                land_finish_second = max(water_finish_first, landStartTime[i]) + landDuration[i]

                ans = min(ans, water_finish, land_finish_second)

        return ans