
from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        s1_count_chars = Counter(s1)
        window_counter = Counter(s2[0:len_s1])

        if s1_count_chars == window_counter:
            return True

        for ii in range(len_s1, len_s2):

            window_counter[s2[ii]] += 1
            window_counter[s2[ii - len_s1]] -= 1

            # needed for equality check between dicts after
            if window_counter[s2[ii - len_s1]] == 0:
                del window_counter[s2[ii - len_s1]]

            if s1_count_chars == window_counter:
                return True

        return False

                


        
        