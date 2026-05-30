

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        char_count = dict()
        max_freq_char = 0

        max_len = 0 # result

        for r in range(len(s)):

            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_freq_char = max(char_count[s[r]], max_freq_char)

            cur_len = r - l + 1

            while (cur_len - max_freq_char) > k:
                char_count[s[l]] -= 1
                l += 1

                cur_len = r - l + 1
            
            max_len = max(max_len, cur_len)
                
        return max_len
                




        