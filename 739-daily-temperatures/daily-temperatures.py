class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i-stack_index

            stack.append((t, i))

        return res
        