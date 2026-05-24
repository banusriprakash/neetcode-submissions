class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        first_word=strs[0]
        last_word=strs[len(strs)-1]

        for i in range(len(first_word)):
            if first_word[i]!=last_word[i]:
                return first_word[0:i]

        return first_word