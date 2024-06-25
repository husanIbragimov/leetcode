def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1

    if n == 1:
        return x

    if n == -1:
        return 1 / x

    answer = myPow(x, n // 2)

    return answer * answer * (x if n % 2 else 1)


x = 2.00000
n = 10
print(myPow(x, n))
x = 2.10000
n = 3
print(myPow(x, n))
