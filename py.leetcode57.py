class Solution:
    """
    Given a set of non-overlapping intervals, insert a new interval into the intervals 
    (merge if necessary).

    You may assume that the intervals were initially sorted according to their start times.
    """

    def insert(self, intervals: "List[List[int]]", newInterval: "List[int]") -> "List[List[int]]":
        ans = []
        addC = 1

        l, r = newInterval[0], newInterval[-1]

        for i in intervals:
            addC2 = 1
            if i[-1] < l:
                ans.append(i)
                addC2 = 0
            if l <= i[-1]:
                if r < i[0]:
                    pass
                else:
                    l = min(l, i[0])
                    addC2 = 0
            if r >= i[0]:
                r = max(r, i[-1])
                addC2 = 0
            if addC and r < i[0]:
                ans.append([l, r])
                addC = 0

            if addC2:
                ans.append(i)
        if addC:
            ans.append([l, r])
        return ans


if __name__ == "__main__":
    a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    b = [9, 20]

    print(Solution().insert(a, b))
