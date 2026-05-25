class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash_set = set(nums)
        longest_sequence = 0

        for elem in hash_set:

            if (elem - 1) not in hash_set:
                count_sequence = 1

                while (elem + count_sequence) in hash_set:
                    count_sequence += 1
            
                longest_sequence = max( longest_sequence, count_sequence)

        return longest_sequence


        

