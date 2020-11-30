from board import Board
from clips import Environment, Symbol

n = int(input())
if (not (4 <= n <= 10)):
    raise Exception("Board size must be 4 <= n <= 10")
state = [[-1 for _ in range(n)] for _ in range(n)]
nBombs = int(input())
bombList = []
for _ in range(nBombs):
    x, y = map(int, input().replace(" ", "").split(","))
    bombList.append((x, y))
board = Board(n, bombList)
board.open(0, 0)
board.print()

# for fact in env.facts():
#     print(fact)
