
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not len(s):
            return 0

        l = 0
        r = 1

        longest = 1
        hash_map = {s[0]: 0}

        while r < len(s):

            if s[r] in hash_map and hash_map[s[r]] >= l:
                l = hash_map[s[r]] + 1
            else:
                longest = max(r-l+1, longest)

            hash_map[s[r]] = r
            r += 1

        return longest

        