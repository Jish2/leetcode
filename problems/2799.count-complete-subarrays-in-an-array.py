class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c = defaultdict(int)
        k = len(Counter(nums))
        n = len(nums)

        l = 0
        ans = 0

        for r in range(l, n):
            c[nums[r]] += 1

            while l < n and len(c) == k:
                c[nums[l]] -= 1
                if not c[nums[l]]: del c[nums[l]]
                l += 1

            ans += l

        return ans
