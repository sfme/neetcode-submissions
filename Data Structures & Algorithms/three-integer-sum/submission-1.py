class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1,len(nums)):
                target = - (nums[i] + nums[j])

                if target in seen:
                    res.add((nums[i], target, nums[j]))
                else:
                    seen.add(nums[j])

        return [list(x) for x in res]
                    






        