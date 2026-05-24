class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hash_map_s = dict()
        for elem in s:
            if elem not in hash_map_s:
                hash_map_s[elem] = 1
            else:
                hash_map_s[elem] += 1

        hash_map_t = dict()
        for elem in t:
            if elem not in hash_map_t:
                hash_map_t[elem] = 1
            else:
                hash_map_t[elem] += 1

        return hash_map_s == hash_map_t
        