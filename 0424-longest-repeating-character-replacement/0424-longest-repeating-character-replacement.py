class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_len = 0
        max_frq = 0

        freq = {}

        for right in range(len(s)):
            
            freq[s[right]] = freq.get(s[right], 0) + 1

            max_frq = max(max_frq, freq[s[right]])

            while (right - left + 1) - max_frq > k:
                freq[s[left]] -= 1
                left += 1

        max_len = max(max_len, right - left + 1)
        
        return max_len