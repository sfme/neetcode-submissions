class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_prod = [0] * len(nums)
        prev_prod = 1
        for idx in range(len(nums)):
            prefix_prod[idx] = prev_prod
            prev_prod *= nums[idx]
            
        suffix_prod = [0] * len(nums)
        post_prod = 1
        for idx in range(len(nums)-1,-1,-1):
            suffix_prod[idx] = post_prod
            post_prod *= nums[idx]
            
        output = [0] * len(nums)
        for idx in range(len(nums)):
            output[idx] = prefix_prod[idx] * suffix_prod[idx]

        return output


