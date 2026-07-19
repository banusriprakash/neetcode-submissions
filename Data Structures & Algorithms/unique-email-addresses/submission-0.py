class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st=set()
        
        for e in emails:
            ls=e.split('@')
            l_n=ls[0].split('+')
            clean_word = l_n[0].replace(".", "")
            clean_word+="@"
            og=(clean_word).join(ls[1])
            print(og)
            st.add(og)

        return len(st)





