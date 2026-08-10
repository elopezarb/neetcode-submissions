class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        set_n = set(nums)
        if len(set_n) < len(nums):
            out = True
        else:
            out = False
        
        return out

