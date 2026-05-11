class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        hash_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        while i<len(s):
            if i<len(s)-1 and hash_map[s[i]]<hash_map[s[i+1]]:
                num += hash_map[s[i+1]]-hash_map[s[i]]
                i+=2
                
            else:
                num+= hash_map[s[i]]
                i+=1
                
        return num