from collections import deque
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_count = n * (n + 1) // 2

        def total_extreme(is_max: bool) -> int:
            stack = []
            total = 0

            for i in range(n + 1):
                current = float("inf") if is_max and i == n else (
                    float("-inf") if i == n else nums[i]
                )

                while stack and (
                    nums[stack[-1]] < current if is_max else nums[stack[-1]] > current
                ):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    total += nums[mid] * (mid - left) * (i - mid)

                stack.append(i)

            return total

        total_range_sum = total_extreme(True) - total_extreme(False)

        def below(limit: int) -> tuple[int, int]:
            if limit <= 0:
                return 0, 0

            max_idx = deque()
            min_idx = deque()
            max_groups = deque()
            min_groups = deque()
            max_suffix_sum = 0
            min_suffix_sum = 0
            count = 0
            range_sum = 0
            left = 0

            for right, value in enumerate(nums):
                while max_idx and nums[max_idx[-1]] <= value:
                    max_idx.pop()
                max_idx.append(right)

                while min_idx and nums[min_idx[-1]] >= value:
                    min_idx.pop()
                min_idx.append(right)

                group_count = 1
                while max_groups and max_groups[-1][0] <= value:
                    group_value, group_size = max_groups.pop()
                    group_count += group_size
                    max_suffix_sum -= group_value * group_size
                max_groups.append([value, group_count])
                max_suffix_sum += value * group_count

                group_count = 1
                while min_groups and min_groups[-1][0] >= value:
                    group_value, group_size = min_groups.pop()
                    group_count += group_size
                    min_suffix_sum -= group_value * group_size
                min_groups.append([value, group_count])
                min_suffix_sum += value * group_count

                while max_idx and min_idx and nums[max_idx[0]] - nums[min_idx[0]] >= limit:
                    if max_idx[0] == left:
                        max_idx.popleft()
                    if min_idx[0] == left:
                        min_idx.popleft()

                    max_groups[0][1] -= 1
                    max_suffix_sum -= max_groups[0][0]
                    if max_groups[0][1] == 0:
                        max_groups.popleft()

                    min_groups[0][1] -= 1
                    min_suffix_sum -= min_groups[0][0]
                    if min_groups[0][1] == 0:
                        min_groups.popleft()

                    left += 1

                count += right - left + 1
                range_sum += max_suffix_sum - min_suffix_sum

            return count, range_sum

        def at_least(limit: int) -> tuple[int, int]:
            small_count, small_sum = below(limit)
            return total_count - small_count, total_range_sum - small_sum

        low, high = 0, max(nums) - min(nums)
        while low < high:
            mid = (low + high + 1) // 2
            count, _ = at_least(mid)
            if count >= k:
                low = mid
            else:
                high = mid - 1

        threshold = low
        greater_count, greater_sum = at_least(threshold + 1)
        return greater_sum + (k - greater_count) * threshold

