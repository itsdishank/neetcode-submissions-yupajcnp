class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        
        for i, (c1, c2) in enumerate(zip(s, t)):
            if map_s.get(c1) != map_t.get(c2):
                return False
            map_s[c1] = i
            map_t[c2] = i
            
        return True