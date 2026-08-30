class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0
        dic_str = {}
        max_freq = 0
        
        for R in range(len(s)):
            if s[R] not in dic_str:
                dic_str[s[R]] = 1
            else:
                dic_str[s[R]] += 1
            
            max_freq = max(dic_str[s[R]], max_freq)
            
            valid_mask = R-L+1 - max_freq <= k
            
            while not valid_mask:
                dic_str[s[L]] -= 1
                L += 1
                max_freq = max(dic_str[s[R]], max_freq)
                valid_mask = R-L+1 - max_freq <= k
            
        return R-L+1