

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        prev_row = [poured]

        for row in range(1, query_row + 1):
            curr_row = [0] * (row + 1)

            for i in range(len(prev_row)):
                extra_amount = prev_row[i] - 1
                if extra_amount > 0:
                    curr_row[i] += extra_amount/2
                    curr_row[i+1] += extra_amount/2

            prev_row = curr_row

        return min(1, prev_row[query_glass])


print(Solution().champagneTower(poured=2, query_row=1, query_glass=1))
