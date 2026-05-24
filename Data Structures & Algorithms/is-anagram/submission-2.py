class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hash_map_s = dict()
        hash_map_t = dict()

        for elem_s, elem_t in zip(s, t):
            hash_map_s[elem_s] = hash_map_s.get(elem_s, 0) + 1
            hash_map_t[elem_t] = hash_map_t.get(elem_t, 0) + 1
            
        return hash_map_s == hash_map_t
        