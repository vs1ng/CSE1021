#!/bin/python3
def is_pronic(n: int) -> bool:
    factors: bytearray = bytearray()
    for i in range(1,n):
        if n%i==0:
            factors.append(i)
    factors.remove(1)
    if len(factors) == 0:
        print("number is prime")
        return False
    else:
        for factor in factors:
            currentpos=factors.index(factor)
            if factor == factors[-1]:
                return False
            else:
                nextfactor: int = factors[currentpos+1]
            if factor*nextfactor==n:
                return True
            else:
                return False
