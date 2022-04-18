def staircase(steps: int) -> int:
    # Figuring out the base case:
    # We could do:
    # return 0 if n < 0, 0 if n == 0, 1 if n == 1, 2 if n == 2, 4 if n == 3

    # We want to get everything covered until the argument of staircase(steps - 3),
    # so steps - 3, is > 0
    # If we have 1 step, there is only 1 possibility to cover
    # if steps == 1:
    #     return 1
    # 1. staircase(0) (sc) would calculate as sc(-1) + sc(-2) + sc(-3), where sc(n < 0)
    # should always return 0 for any n < 0

    # 2. sc(1) would calculate as sc(0) + sc(-1) + sc(-2)
    # because sc(-1) and sc(-2) return 0, and sc(1) must yield 1
    # sc(0) must return 1
    if steps < 0:
        return 0
    if steps == 0 or steps == 1:
        return 1

    # 3. sc(2) would calculate as sc(1) + sc(0) + sc(-1),
    # which yields 1 + 1 = 2, which is correct

    # 4. sc(3) would calculate as sc(2) + sc(1) + sc(0)
    # which yields 2 + 1 + 1 = 4, which again, is correct

    return staircase(steps - 1) + staircase(steps - 2) + staircase(steps - 3)


print(staircase(10))
