from itertools import permutations


def rule_bomb():
    rules = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            rule = ""
            if (x == 0 and y == 0):
                continue
            rule += f"(defrule check-3x3-1-{x}-{y}"
            rule += f"(new-x-pos $? ?xm1 ?x ?x1 $?)(new-y-pos $? ?ym1 ?y ?y1 $?)"
            rule += f"(is-1 ?x ?y)"
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if ((dx == 0 and dy == 0)):
                        continue
                    closed = dx == x and dy == y
                    coord = f"{'?xm1' if dx == -1 else '?x' if dx == 0 else '?x1'} {'?ym1' if dy == -1 else '?y' if dy == 0 else '?y1'}"
                    if (closed):
                        rule += f"?f <- (is-unknown {coord})"
                    else:
                        rule += f"(or (is-open {coord})(is-edge {coord})(is-safe {coord}))"
                        rule += f"(not (is-bomb {coord}))"
            rule += f" => "
            coord = f"{'?xm1' if x == -1 else '?x' if x == 0 else '?x1'} {'?ym1' if y == -1 else '?y' if y == 0 else '?y1'}"
            rule += f"(assert (is-bomb {coord}))"
            rule += f"(retract ?f)"
            rule += f")"
            rules.append(rule)
    return rules


def rule_safe():
    rules = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            rule = ""
            if (x == 0 and y == 0):
                continue
            rule += f"(defrule check-3x3-1-safe-{x}-{y}"
            rule += f"(new-x-pos $? ?xm1 ?x ?x1 $?)(new-y-pos $? ?ym1 ?y ?y1 $?)"
            rule += f"(is-1 ?x ?y)"
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if ((dx == 0 and dy == 0)):
                        continue
                    bomb = dx == x and dy == y
                    coord = f"{'?xm1' if dx == -1 else '?x' if dx == 0 else '?x1'} {'?ym1' if dy == -1 else '?y' if dy == 0 else '?y1'}"
                    if (bomb):
                        rule += f"(is-bomb {coord})"
                    else:
                        rule += f"(or (is-open {coord})(is-closed {coord}))"
            rule += f" => "
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if ((dx == 0 and dy == 0)):
                        continue
                    coord = f"{'?xm1' if dx == -1 else '?x' if dx == 0 else '?x1'} {'?ym1' if dy == -1 else '?y' if dy == 0 else '?y1'}"
                    rule += f"(assert (is-safe {coord}))"
            rule += f")"
            rules.append(rule)
    return rules


def add3x3rules(env):
    for rule in rule_bomb():
        env.build(rule)
    for rule in rule_safe():
        env.build(rule)
