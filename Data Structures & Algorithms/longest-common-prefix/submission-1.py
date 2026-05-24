class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        strs=sorted(strs)
        first_word=strs[0]
       
        for j in range(len(first_word)):

            for i in range(1,len(strs)):
                current_word=strs[i]

                if j>=len(current_word) or current_word[j]!=first_word[j]:
                    return first_word[0:j]

                else:
                    break

        return first_word

        