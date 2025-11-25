#!/bin/python3
class DIVISORCOUNTER:
    def __init__(self):
        pass

    def count_divisors(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        total_divisors = 1
        
        exponent = 0
        while n % 2 == 0:
            exponent += 1
            n //= 2
        
        if exponent > 0:
            total_divisors *= (exponent + 1)

        i = 3
        while i * i <= n:
            exponent = 0
            while n % i == 0:
                exponent += 1
                n //= i
            
            if exponent > 0:
                total_divisors *= (exponent + 1)
                
            i += 2

        if n > 1:
            total_divisors *= 2
            
        return total_divisors
