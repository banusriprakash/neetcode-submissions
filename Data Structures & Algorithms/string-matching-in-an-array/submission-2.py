class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        words.sort(key=len)
        ls=[]

        for i in range(len(words)):
            s=words[i]
            for val in words[1:]:

                if len(val)==len(s):
                    continue

                if s in val:
                    ls.append(s)
                    break

        return ls
        