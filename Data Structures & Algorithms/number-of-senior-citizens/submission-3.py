class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt=0
        for val in details:
            st=int(val[11:13])
            if st > 60:
                cnt+=1

        return cnt
        