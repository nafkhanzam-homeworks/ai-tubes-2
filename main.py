from board import Board

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
print("==== ACTUAL ====")
board.secret_print()
print("==== CURRENT ====")
board.print()
safe_cells = [(0, 0)]
print("Safe cells:")
for cell in safe_cells:
    print(cell)

while len(safe_cells) > 0:
    (x, y) = safe_cells[0]
    print(f"Opening ({x}, {y})")
    board.open(x, y)
    board.print()
    safe_cells = board.solve_get_safe_cells()
    print("Safe cells:")
    for cell in safe_cells:
        print(cell)
