class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        sub_set = set()
        res = 0
        for j in range(len(s)):
            while s[j] in sub_set:
                sub_set.remove(s[i])
                i+=1
            sub_set.add(s[j])
            res = max(res, j-i+1)
        return res