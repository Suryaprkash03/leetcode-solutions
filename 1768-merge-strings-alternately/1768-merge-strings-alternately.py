class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            res = ''.join(a + b for a, b in zip(word1, word2))
            return res + word1[len(word2):] + word2[len(word1):]