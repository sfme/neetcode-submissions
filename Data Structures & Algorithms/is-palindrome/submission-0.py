class Solution:

    def isPalindrome(self, s: str) -> bool:

        p_left = 0
        p_right = len(s) - 1

        while p_left < p_right:

            if not s[p_left].isalnum():
                p_left += 1
                continue

            if not s[p_right].isalnum():
                p_right -= 1
                continue

            if s[p_left].lower() != s[p_right].lower():
                return False

            p_left += 1
            p_right -= 1

        return True


            

            



        