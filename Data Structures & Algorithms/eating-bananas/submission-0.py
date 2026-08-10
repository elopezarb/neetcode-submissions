class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def roundUp(n, div):
            if n%div == 0:
                return n//div
            else:
                return n//div + 1
        left = 1 
        right = max(piles)
        
        while left<= right:
            mid = (left + right) // 2
            
            sum_pile = sum(roundUp(pile, mid) for pile in piles)
            if sum_pile <= h:
                right = mid - 1
            
            elif sum_pile > h:
                left = mid + 1
            
        return left
