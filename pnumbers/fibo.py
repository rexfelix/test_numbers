def fibo(n: int):
    if n < 1:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
