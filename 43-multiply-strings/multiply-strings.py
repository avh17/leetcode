class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0]*(m+n)

        for i in range(m-1, -1, -1):
            carry = 0
            for j in range(n-1, -1, -1):
                temp_sum = (ord(num1[i])-ord("0"))*(ord(num2[j])-ord("0"))+res[i+j+1]+carry
                res[i+j+1]=temp_sum%10
                carry = temp_sum//10

            res[i] += carry

        result = "".join(map(str, res))
        result = result.lstrip("0")
        return result if result else "0"