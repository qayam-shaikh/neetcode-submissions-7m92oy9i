class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        fives,tens=0,0
        for x in bills:
            if x==5:
                fives+=1
            elif x==10:
                if fives>0:
                    fives-=1
                else:
                    return False
                tens+=1
            else:
                if fives >0 and tens>0:
                    fives-=1
                    tens-=1
                elif fives>2:
                    fives-=3
                else:
                    return False
        return True