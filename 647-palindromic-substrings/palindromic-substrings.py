class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count+=self.countPali(s, i, i) + self.countPali(s, i, i+1)
        return count

    def countPali(self, s, l, r) -> int:
        res = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res