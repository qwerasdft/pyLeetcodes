class Solution:
    """
    Given a collection of intervals, merge all overlapping intervals.
    """

    def merge(self, intervals: "List[List[int]]") -> "List[List[int]]":
        arr1 = sorted(intervals, key=lambda i: i[0])
        ans = []

        for i in arr1:
            if ans and i[0] <= ans[-1][-1]:
                ans[-1][-1] = max(i[-1], ans[-1][-1])
            else:
                ans.append(i)
        return ans


if __name__ == "__main__":
    a = [[1, 3], [2, 6], [8, 10], [15, 18]]

    print(Solution().merge(a))
