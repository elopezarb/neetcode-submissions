class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        operations = []
        nums.sort()
        
        
        for k in range(len(nums)):
            left = k+1 ; right = len(nums)-1
            if k-1 != -1 and nums[k-1]==nums[k]:
                continue
            while left < right:
                sum1 = nums[k] + nums[left] + nums[right]
                ope = [nums[k], nums[left], nums[right]]
                    
                if sum1 == 0:
                    if ope not in operations:
                        operations.append([nums[k], nums[left], nums[right]])
                        
                    left+= 1
                    right += -1
                    continue
                
                
                elif sum1 < 0:
                    left += 1
                    continue
                
                elif  sum1 > 0:
                    right += -1
                    continue
        
        return operations