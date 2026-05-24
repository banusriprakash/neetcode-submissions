class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0

        for st in details:
            num=int(st[11:13])
            if num>60:
                cnt+=1

        return cnt
        