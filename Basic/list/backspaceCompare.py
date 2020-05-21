class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1, t1 = [], []
        for s in S:
            if s == '#':
                if len(s1):
                    s1.pop()
            else:
                s1.append(s)

        for t in T:
            if t == '#':
                if len(t1):
                    t1.pop()
            else:
                t1.append(t)

        return s1 == t1

obj = Solution()
obj.backspaceCompare("a##c", "#a#c")