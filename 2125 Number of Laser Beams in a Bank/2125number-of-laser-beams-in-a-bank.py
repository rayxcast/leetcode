class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        r1Dev = 0
        totalDevs = 0
        for row in bank:
            #check for devices in row
            devs = 0 
            for dev in row:
                if dev == "1":
                    devs += 1 # found device adding it
            if devs > 0:
                if r1Dev <= 0: # if 0 then there is not row 1 one saved
                    r1Dev = devs
                else: # if not 0 then there is a row 1 and we found a row 2
                    totalDevs += r1Dev * devs # calculate the laser beans in between r1 and r2
                    r1Dev = devs # now then row 2 becomes row 1 to check for the next row 
        
        return totalDevs
            





        