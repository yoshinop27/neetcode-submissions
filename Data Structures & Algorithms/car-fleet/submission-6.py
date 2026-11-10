class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hm = {}
        fleets = 0
        for pos, sp in zip(position, speed):
            hm[pos] = sp
        # iterate through both pos and speed
        position.sort()
        i = len(position) - 1
        while i >= 0: 
            # set values 
            pos = position[i] 
            spd = hm[pos] 
            next_pos = position[i-1] 
            next_spd = hm[next_pos] 
            temp = 1
            # identify if fleet between current and next
            while i-temp>-1 and (target-pos)/spd >= (target-next_pos)/next_spd: 
                temp += 1
                next_pos = position[i-temp] 
                next_spd = hm[next_pos]
            fleets += 1
            i -= temp
        return fleets
            
        

