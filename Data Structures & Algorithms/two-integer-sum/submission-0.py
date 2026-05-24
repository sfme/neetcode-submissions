class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = dict()

        for cur_idx, elem_val in enumerate(nums):

            delta_val = (target - elem_val)

            if delta_val in hash_map:
                return [hash_map[delta_val], cur_idx]
            else:
                hash_map[elem_val] = cur_idx
