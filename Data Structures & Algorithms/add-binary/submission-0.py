class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=a[::-1],b[::-1]
        res,c='',0
        for i in range(max(len(a),len(b))):
            dA=int(a[i]) if i<len(a) else 0
            dB=int(b[i]) if i<len(b) else 0
            t=dA+dB+c
            char=str(t%2)
            res = char + res
            c=t//2
        if c:
            res = '1'+res
        return res






