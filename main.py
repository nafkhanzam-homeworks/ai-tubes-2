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

while len(safe_cells) > 0:
    valid_cells = []
    for cell in safe_cells:
        (x, y) = cell
        res = board.open(x, y)
        if (res):
            print(f"Opening ({cell})")
            valid_cells.append(cell)
    if (len(valid_cells) == 0):
        print("Tidak ada safe-cell baru yang masih tertutup")
        break
    board.print()
    (safe_cells, bomb_cells) = board.solve()
    print("Safe cells:")
    for cell in safe_cells:
        print(cell)
    print("Bomb cells:")
    for cell in bomb_cells:
        print(cell)
