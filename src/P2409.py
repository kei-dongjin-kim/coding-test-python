class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        NOD = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def next(val: str) -> str:
            m = int(val[0:2])
            d = int(val[3:5])
            if d == NOD[m]:
                d = 1
                if m == 12:
                    m = 1
                else:
                    m += 1
            else:
                d += 1
            return f'{m:02d}-{d:02d}'
        
        alice = []
        while True:
            alice.append(arriveAlice)
            if arriveAlice == leaveAlice:
                break
            else:
                arriveAlice = next(arriveAlice)
        
        count = 0
        while True:
            if arriveBob in alice:
                count += 1
            if arriveBob == leaveBob:
                break
            else:
                arriveBob = next(arriveBob)
        
        return count
