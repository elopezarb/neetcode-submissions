class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right = rows*cols -1
       
        while left <= right:
            mid = (left + right)//2
            
            min_val = matrix[mid//cols][mid%cols] 
            if min_val> target:
                right = mid -1
            elif min_val < target:
                left = mid +1
            
            else:
                return True
            
        
        return False