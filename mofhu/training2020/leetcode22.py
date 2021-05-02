class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = "("
        l, r = n-1, n
        def iter_ans(s, l, r):
            if l == 0 and r == 1:
                ans.append(s+')')
                return
            if l >= 1:
                iter_ans(s+'(', l-1, r)
            if l < r:
                iter_ans(s+')', l, r-1)
        iter_ans(s, l, r)
        return ans

