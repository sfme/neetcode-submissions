class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:

        exists_set = set()

        for elem in nums:
            if elem in exists_set:
                return True
                
            exists_set.add(elem)

        return False
        