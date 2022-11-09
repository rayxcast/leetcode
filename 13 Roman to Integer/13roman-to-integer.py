# So let's as always try to solve it with brute force
# Let's use for loops to check each character and also by checking the next char on special cases
# If the adjacent char is a V, X, L, C, D, or M then we know that those two characters represent a single number. Ex CD is 400
# If this is found then we will increase the next iteration by 2, so this way we skip the said adjacent character which represent
# This special case only happens for I, X, and C, so we only need to check for the next char when these char are present

class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0;
        i = 0;
        while i < (len(s)):
            match s[i]:
                case 'I':
                    if (i+1) < len(s) and (s[i+1] == 'V'):
                        number += 4
                        i += 2
                    elif (i+1) < len(s) and (s[i+1] == 'X'):
                        number += 9 
                        i += 2
                    else:
                        number += 1
                        i += 1
                case 'V':
                    number += 5
                    i += 1
                case 'X':
                    if (i+1) < len(s) and (s[i+1] == 'L'):
                        number += 40
                        i += 2
                    elif (i+1) < len(s) and (s[i+1] == 'C'):
                        number += 90 
                        i += 2
                    else:
                        number += 10
                        i += 1
                case 'L':
                    number += 50
                    i += 1
                case 'C':
                    if (i+1) < len(s) and (s[i+1] == 'D'):
                        number += 400
                        i += 2
                    elif (i+1) < len(s) and (s[i+1] == 'M'):
                        number += 900  
                        i += 2
                    else:
                        number += 100
                        i += 1
                case 'D': 
                    number += 500
                    i += 1
                case 'M':
                    number += 1000
                    i += 1
                case _:
                    i += 1
                    print('Not match found.')
        
        return number
                
        