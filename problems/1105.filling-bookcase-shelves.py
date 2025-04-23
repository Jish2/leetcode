#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

from typing import List

# @lc code=start


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [[float("inf") for _ in range(shelfWidth + 1)] for _ in range(n)]

        def dfs(i, sw, mh):
            thickness, height = books[i]
            new_h = max(mh, height)
            if i == n - 1:
                if sw - thickness < 0:
                    # create new row
                    return mh + height
                else:
                    # otherwise add current row
                    return new_h

            if dp[i][sw] != float("inf"):
                return dp[i][sw]

            # same line case
            a = float("inf")
            if sw - thickness >= 0:
                a = dfs(i + 1, sw - thickness, new_h)

            # new line case
            b = mh + dfs(i + 1, shelfWidth - thickness, height)

            res = min(a, b)
            dp[i][sw] = res
            return res

        return dfs(0, shelfWidth, 0)


# @lc code=end

# print(
#     Solution().minHeightShelves(
#         books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4
#     )
# )
print(
    Solution().minHeightShelves(books=[[7, 3], [8, 7], [2, 7], [2, 5]], shelfWidth=10)
)
