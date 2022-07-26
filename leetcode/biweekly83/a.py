# author: mofhu@github
# 6128. Best Poker Hand

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # flush
        lens = set()
        for i in suits:
            if i not in lens:
                lens.add(i)
        if len(lens) == 1:
            return 'Flush'
        ranks.sort()
        lenr = {}
        for i in ranks:
            if i not in lenr:
                lenr[i] = 1
            else:
                lenr[i] += 1
        maxr = 1
        for key in lenr:
            if lenr[key] > maxr:
                maxr = lenr[key]
        if maxr >= 3:
            return 'Three of a Kind'
        elif maxr == 2:
            return 'Pair'
        else:
            return 'High Card'
