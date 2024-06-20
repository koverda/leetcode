def mySqrt(x: int) -> int:
    l = 1
    r = x

    while l <= r:
        m = (l + r) // 2

        if m * m > x:
            r = m - 1
        elif m * m < x:
            l = m + 1
        else:
            return m

    return (l + r) // 2

print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(3))
print(mySqrt(4))
print(mySqrt(5))
print(mySqrt(6))
print(mySqrt(7))
print(mySqrt(8))
print(mySqrt(9))