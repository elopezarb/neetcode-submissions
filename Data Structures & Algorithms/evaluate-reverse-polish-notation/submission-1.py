from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = []
        for int0 in tokens:

            
            if int0 in {'+', '-', '*', '/'}:
                int1 = operations.pop()
                int2 = operations.pop()
                
                if int0 == '+':
                    int_0 = int1 + int2
                if int0 == '*':
                    int_0 = int2 * int1
                if int0 == '/':
                    if int1*int2>0:
                        int_0 = int2//int1
                    else:
                        int_0 = abs(int2)//abs(int1)*-1
                if int0 == '-':
                    int_0 = int2 - int1
            else:
                int_0 = int(int0)
            
            operations.append(int_0)
     
        return operations[-1]