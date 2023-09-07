class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        instructions = [0]*len(s)
        for i in range(len(s)):
            currPos = startPos.copy()
            # print("Start Position", startPos)
            # print("starting at", s[i])
            for move in s[i:]:
                if(move == 'R'): 
                    currPos[1] += 1 # move column 
                elif (move == 'L'):
                    currPos[1] -= 1 # move column 
                elif (move == 'D'):
                    currPos[0] += 1 # move row 
                elif (move == 'U'):
                    currPos[0] -= 1 # move row
                # print(move, currPos)
                if(currPos[0] >= 0 and currPos[0] < n and currPos[1] >= 0 and currPos[1] < n):
                    instructions[i] += 1
                else: 
                    break
            
            # print("\n")
        
        return instructions
                
