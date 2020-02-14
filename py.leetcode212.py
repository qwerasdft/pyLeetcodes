class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':

        trid = {}

        for word in words:
            p = trid
            for ch in word:
                if ch not in p:
                    p[ch] = {}
                p = p[ch]
            p['#'] = '#'

        h = len(board)
        w = len(board[0])
        res = []

        def check(board, i, j, p, wtmp):
            nonlocal res, h, w
            tmp = ''

            if "#" in p and p['#'] == '#':

                p['#'] = 'x'
                return res.append(wtmp)

            if i < 0 or j < 0 or i >= h or j >= w:
                return
            if board[i][j] not in p:
                return
            p = p[board[i][j]]

            tmp, board[i][j] = board[i][j], tmp

            check(board, i+1, j, p, wtmp+tmp)
            check(board, i-1, j, p, wtmp+tmp)
            check(board, i, j+1, p, wtmp+tmp)
            check(board, i, j-1, p, wtmp+tmp)

            tmp, board[i][j] = board[i][j], tmp

        for i in range(h):
            for j in range(w):
                if board[i][j] in trid:
                    check(board, i, j, trid, '')
        return res


if __name__ == "__main__":
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]

    print(Solution().findWords(board, words))
