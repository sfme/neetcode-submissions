
from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        s1_count_chars = Counter(s1)
        window_arr = list(s2[0:len_s1])

        if s1_count_chars == Counter(window_arr):
            return True

        for ii in range(len_s1, len_s2):

            window_arr.append(s2[ii])
            window_arr.pop(0)

            if s1_count_chars == Counter(window_arr):
                return True

        return False

                


        
        