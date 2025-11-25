def is_abundant(n: int) -> bool:
    ProperDivisors: bytearray = bytearray(len(str(n)))
    for i in range(2,n):
        if n%i==0:
            ProperDivisors.append(i)
        else:
            continue
    S: int = 0
    for I in ProperDivisors:
        S+=I
    if S > n:
        return True
    else:
        return False
