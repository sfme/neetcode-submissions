
from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        s1_count_chars = Counter(s1)

        for cur in range(len_s2-len_s1+1):
            s2_count_chars = Counter(s2[cur:(cur + len_s1)])

            if s1_count_chars == s2_count_chars:
                return True

        return False

                


        
        