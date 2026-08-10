class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0; right = len(s)-1
        
        while left < right:
            if not (s[left].isalpha() or s[left].isnumeric()):
                left += 1
                continue
            elif not (s[right].isalpha() or s[right].isnumeric()):
                right += -1
                continue
            
            elif s[left].lower() != s[right].lower():
                
                return False
            left += 1
            right += -1
        
        return True