class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def heapify(stones):
            stones.append(stones[0])
            cur = (len(stones)-1)//2
            while cur > 0:
                i = cur
                while i*2 < len(stones):
                    if i*2+1 < len(stones) and stones[i*2+1] > stones[i] and stones[i*2+1] > stones[i*2]:
                        stones[i], stones[i*2+1] = stones[i*2+1], stones[i]
                        i = i * 2 + 1
                    elif stones[i*2] > stones[i]:
                        stones[i], stones[i*2] = stones[i*2], stones[i]
                        i = i * 2
                    else:
                        break
                cur -= 1
            return stones
        
        def popH(stones):
            if len(stones) == 1:
                return
            if len(stones) == 2:
                return stones.pop()
            
            ret = stones[1]
            stones[1] = stones.pop()
            cur = 1  
            while cur*2 < len(stones):
                if cur*2+1 < len(stones) and stones[cur*2+1] > stones[cur] and stones[cur*2+1] > stones[cur*2]:
                    stones[cur], stones[cur*2+1] = stones[cur*2+1], stones[cur]
                    cur = cur * 2 + 1
                elif stones[cur*2] > stones[cur]:
                    stones[cur], stones[cur*2] = stones[cur*2], stones[cur]
                    cur = cur * 2
                else:
                    break
            return ret

        def pushH(stones, val):
            stones.append(val)
            cur = len(stones) - 1
            while cur // 2 > 0:
                if stones[cur] > stones[cur//2]:
                    stones[cur], stones[cur//2] = stones[cur//2], stones[cur]
                    cur = cur // 2
                else:
                    break

        stones = heapify(stones)
        while len(stones) > 2:
            x = popH(stones)
            y = popH(stones)
            if x < y:
                pushH(stones, y-x)
            elif x > y:
                pushH(stones, x-y)
        if len(stones) == 2:
            return stones[1]
        else:
            return 0


        