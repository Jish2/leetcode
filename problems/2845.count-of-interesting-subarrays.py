class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        c = 0
        ans = 0
        hm = defaultdict(int)
        hm[0] += 1

        for num in nums:
            if num % modulo == k: c += 1
            ans += hm[(c - k + modulo) % modulo]
            hm[c % modulo] += 1

        return ans


        # 01123
        #  ^^
        # ^   ^

