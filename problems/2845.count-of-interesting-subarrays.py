class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        p = [0] * n
        c = 0
        for i, num in enumerate(nums):
            if num % modulo == k: c += 1
            p[i] = c

        ans = 0

        for r in range(n):
            if p[r] % modulo == k:
                ans += ceil(p[r] / modulo)

        return ans


        # 01123
        #  ^^
        # ^   ^
