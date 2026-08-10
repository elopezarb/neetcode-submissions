class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        hash_str = {}
        for st in strs:
            sort_st = ''.join(sorted(st))
            if not hash_str.get( sort_st, False):
                hash_str[sort_st]  = [st]
            else:
                hash_str[sort_st] += [st]
        
        list_out = []
        for k, v in hash_str.items():
            list_out.append(v)
            
        
        return list_out
        
        
        



        



