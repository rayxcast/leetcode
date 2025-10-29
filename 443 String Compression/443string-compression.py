class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        if len(chars) == 1:
            return 1
        
        currIndex = 0
        currChar = chars[currIndex]
        count = 1
        for i in range(1, len(chars)):
            # print("curr chart:", chars[i])
            if (chars[i] != currChar and i < (len(chars)-1)) or (chars[i] == currChar and i == (len(chars)-1)): # new char found set and reset count and move to next char
                if i == (len(chars)-1):
                    count+=1
                chars[currIndex] = currChar
                currChar = chars[i]
                if count > 1 and count <= 9:
                    currIndex+=1
                    chars[currIndex] = str(count)
                elif count > 9:
                    sCount = str(count)
                    for i in range(len(sCount)):
                        currIndex = currIndex+1
                        chars[currIndex] = sCount[i]
                count = 1
                currIndex+=1
            elif chars[i] != currChar and i == (len(chars)-1):
                chars[currIndex] = currChar
                currChar = chars[i]
                if count > 1 and count <= 9:
                    currIndex+=1
                    chars[currIndex] = str(count)
                elif count > 9:
                    sCount = str(count)
                    for i in range(len(sCount)):
                        currIndex = currIndex+1
                        chars[currIndex] = sCount[i]
                count = 1
                currIndex+=1
                chars[currIndex] = currChar
                currIndex+=1
            else:    
                count+=1

        # print("currIndex:", currIndex)      
        # print("chars:", chars[:currIndex])      
        return currIndex