class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map1, count_map2 = {}, {}

        for c in s:
            count_map1[c] = 1+count_map1.get(c,0)

        for r in t:
            count_map2[r] = 1+count_map2.get(r,0)

        return count_map1==count_map2