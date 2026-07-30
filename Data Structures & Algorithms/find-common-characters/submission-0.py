class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        
        other_words=[list(w) for w in words[1:]]

        st=[]
        sr=words[0]
        for i in range(len(sr)):
            swp=True
            for j in range(len(other_words)):
                if sr[i] in other_words[j]:
                    other_words[j].remove(sr[i])
                else:
                    swp=False
                    break
            if swp:
                st.append(sr[i])

        return st