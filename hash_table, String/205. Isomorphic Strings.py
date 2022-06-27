class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        processed = {}
        for i in range(len(s)):
            if s[i] not in processed and t[i] not in processed.values():
                processed[s[i]] = t[i]
            else:
                if processed.get(s[i]) != t[i]:
                    return False
        return True