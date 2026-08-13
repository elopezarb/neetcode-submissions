class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        length = 0
        
        str_set = set()
        
        for R in range(len(s)):
            
            while s[R] in str_set:
                str_set.remove(s[L])
                L += 1
                
                
            
            str_set.add(s[R])
            length = max(length, R-L+1)
                
        
        return length