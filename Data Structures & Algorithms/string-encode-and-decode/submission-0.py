class Solution:

    def encode(self, strs: List[str]) -> str:

        new_str = ''
        for st in strs:
            new_str += '#' + str(1000+len(st))[1:] + st
        
        return new_str

    def decode(self, s: str) -> List[str]:
        strs = []
        l_s = 0
        while l_s < len(s)-1:
            st = s[l_s]
            if st == '#':
                _three = int(s[l_s+1:l_s+3+1])
                
                st_n = s[l_s+4: l_s+4 + _three]
                l_s += _three+3
                strs.append(st_n)
                l_s += 1
        
        return strs

            



