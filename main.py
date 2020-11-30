from clips import Environment, Symbol

environment = Environment()
environment.load("minesweeper.clp")

# n = int(input())
# if (not (4 <= n <= 10)):
#     raise Exception("Board size must be 4 <= n <= 10")
# state = [[-1 for _ in range(n)] for _ in range(n)]
# nBombs = int(input())
# bombList = []
# for _ in range(nBombs):
#     x, y = map(int, input().replace(" ", "").split(","))
#     bombList.append((x, y))

environment.assert_string(f"(coord 0 0 1)")
environment.assert_string(f"(coord 1 0 1)")
environment.assert_string(f"(coord 0 1 1)")
environment.assert_string(f"(coord 0 2 -1)")
environment.assert_string(f"(coord 2 0 -1)")
environment.assert_string(f"(coord 1 1 -1)")
environment.assert_string(f"(coord 1 2 -1)")
environment.assert_string(f"(coord 2 1 -1)")
environment.assert_string(f"(coord 2 2 -1)")
environment.run()
