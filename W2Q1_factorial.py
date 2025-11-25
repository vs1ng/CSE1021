def factorial(n: int) -> int:
    k: int = 1
    for i in range(n,0,-1):
        k *= i
    return k

