class Solution:
    def countLargestGroup(self, n: int) -> int:
        c = defaultdict(int)
        for i in range(1, n + 1):
            k = sum(c for c in map(int, str(i)))
            c[k] += 1
        mxv = max(c.values())
        ans = 0
        for k, v in c.items():
            if v == mxv: ans += 1
        return ans
