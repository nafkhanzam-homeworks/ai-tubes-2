from clips.environment import Environment
import re

# states
UNKNOWN = -1
FLAGGED = -2
# 0 1 2 3 4


class Board:
    def __init__(self, n, bombs):
        self.n = n
        self.init_secret(bombs)
        self.init_board()

    def init_secret(self, bombs):
        self.secret = [[UNKNOWN for _ in range(self.n)] for _ in range(self.n)]
        for (x, y) in bombs:
            self.secret[x][y] = FLAGGED
        for x in range(self.n):
            for y in range(self.n):
                if (self.secret[x][y] == UNKNOWN):
                    self.secret[x][y] = self.secret_count_bombs_in_area(x, y)

    def init_board(self):
        self.board = [[UNKNOWN for _ in range(self.n)] for _ in range(self.n)]

    def secret_count_bombs_in_area(self, x, y):
        res = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (self.secret_is_bomb(x+dx, y+dy)):
                    res += 1
        return res

    def secret_is_bomb(self, x, y):
        if (not self.is_valid(x, y)):
            return False
        return self.secret[x][y] == FLAGGED

    def secret_print(self):
        for x in range(self.n):
            print(" ".join(map(lambda v: " K" if v == UNKNOWN else " B" if v ==
                               FLAGGED else str(v).rjust(2), self.secret[x])))

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def open(self, x, y):
        if (not self.is_valid(x, y) or self.board[x][y] != UNKNOWN):
            return False
        v = self.secret[x][y]
        self.board[x][y] = v
        if (v == 0):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    next_x = x + dx
                    next_y = y + dy
                    if (self.is_valid(next_x, next_y)):
                        self.open(next_x, next_y)
        return True

    def print(self):
        for x in range(self.n):
            print(" ".join(map(lambda v: " K" if v == UNKNOWN else " B" if v ==
                               FLAGGED else str(v).rjust(2), self.board[x])))

    def solve_get_safe_cells(self):
        env = Environment()
        env.load("minesweeper.clp")
        for i in range(self.n):
            env.assert_string(f"(is-edge {i} -1)")
            env.assert_string(f"(is-edge -1 {i})")
            env.assert_string(f"(is-edge {self.n} {i})")
            env.assert_string(f"(is-edge {i} {self.n})")
        env.assert_string(f"(x-pos {' '.join(map(str, range(self.n)))})")
        env.assert_string(f"(y-pos {' '.join(map(str, range(self.n)))})")
        for x in range(self.n):
            for y in range(self.n):
                v = self.board[x][y]
                fact_name = "is-" + str(v)
                if (v == UNKNOWN):
                    fact_name = "is-unknown"
                elif (v == FLAGGED):
                    fact_name = "is-bomb"
                env.assert_string(f"({fact_name} {x} {y})")
                env.assert_string(f"(is-open {x} {y})")
        env.run()
        safes = []
        for fact_str in env.facts():
            fact = re.findall(r"\((.*)\)", str(fact_str))[0].split(" ")
            if (len(fact) != 3):
                continue
            [fact_name, x_str, y_str, *_] = fact
            x, y = int(x_str), int(y_str)
            if (fact_name == "is-safe"):
                safes.append((x, y))
            elif (fact_name == "is-bomb"):
                self.board[x][y] = FLAGGED
        return safes
