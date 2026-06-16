class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for ns in s:
            if "a" <= ns <= "z":
                result.append(ns)
            elif ns == "*":
                if result:
                    result.pop()
            elif ns == "#":
                result.extend(result)
            elif ns == "%":
                result.reverse()
        return "".join(result)
        