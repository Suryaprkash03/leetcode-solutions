class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        left = 0
        
        for right in range(len(s2)):
            window[s2[right]] += 1
            
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                left += 1
                
            if window == need:
                return True
            
        return False