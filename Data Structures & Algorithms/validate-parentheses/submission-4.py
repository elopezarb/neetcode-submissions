class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dic = {'[': ']', '(': ')', '{': '}'}
        pars_l = []
        if len(s) == 0 or len(s)==1:
            return False
        
        
        for par in s:
            
            if par in parenthesis_dic.keys():
                if par == s[-1]:
                    return False
                pars_l.append(par)
                continue
            elif par in parenthesis_dic.values():
                if len(pars_l)==0:
                    return False
                if parenthesis_dic[pars_l.pop()] == par:
                    continue
                else:
                    return False
        
        if len(pars_l) != 0:
            return False

        
        return True
                   