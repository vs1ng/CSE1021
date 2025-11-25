#!/bin/python3
class WEEK7:
    def __init__(self):
        pass

    def lucas_sequence(self, n):
        if n <= 0:
            return bytearray()
        
        sequence = bytearray()
        
        a, b = 2, 1 

        if n >= 1:
            if a > 255:
                return bytearray()
            sequence.append(a)
        
        if n >= 2:
            if b > 255:
                return bytearray()
            sequence.append(b)
        
        i = 3
        while i <= n:
            next_lucas = a + b
            if next_lucas > 255:
                return sequence
            sequence.append(next_lucas)
            a = b
            b = next_lucas
            i += 1
            
        return sequence

    def is_perfect_power(self, n):
        if n <= 1:
            return False
        
        max_exponent = 1
        temp_n = n
        while temp_n > 1:
            temp_n //= 2
            max_exponent += 1
            
        exponent = 2
        while exponent < max_exponent:
            
            low = 2
            high = n
            
            root = 0
            while low <= high:
                mid = (low + high) // 2
                
                power = 1
                for _ in range(exponent):
                    power *= mid
                    if power > n:
                        break

                if power == n:
                    return True
                elif power < n and power > 0:
                    low = mid + 1
                    root = mid
                else:
                    high = mid - 1
            
            exponent += 1
            
        return False

    def collatz_length(self, n):
        if n <= 0:
            return 0
        
        steps = 0
        current = n
        
        while current != 1:
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
            steps += 1
            
        return steps

    def polygonal_number(self, s, n):
        if s < 3 or n <= 0:
            return 0
            
        s_minus_2 = s - 2
        s_minus_4 = s - 4
        
        numerator = s_minus_2 * n * n - s_minus_4 * n
        return numerator // 2

    def _extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        
        g, x1, y1 = self._extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _mod_exp(self, base, exponent, modulus):
        if modulus == 1:
            return 0
        
        res = 1
        base %= modulus
        
        while exponent > 0:
            if exponent % 2 == 1:
                res = (res * base) % modulus
            
            base = (base * base) % modulus
            exponent //= 2
            
        return res

    def _is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_carmichael(self, n):
        if self._is_prime(n) or n % 2 == 0 or n < 561:
            return False
        
        for a in range(2, n):
            if self._gcd(a, n) == 1:
                if self._mod_exp(a, n - 1, n) != 1:
                    return False
        
        return True
