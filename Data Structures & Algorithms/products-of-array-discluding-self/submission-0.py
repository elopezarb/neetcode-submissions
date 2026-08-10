class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod_left = [1]
        prod_left = 1
        for n in nums[:-1]:
            prod_left *= n
            l_prod_left.append(prod_left)
        
        l_prod_right = [1]
        prod_right = 1
        for i in range(len(nums)-1, 0, -1):
            prod_right *= nums[i]
            l_prod_right = [prod_right] + l_prod_right
            
        prods = []
        for x,y in zip(l_prod_left, l_prod_right):
            prods.append(x*y)
        
        
        return prods