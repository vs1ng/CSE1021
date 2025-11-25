#!/bin/python3
class WEEK6:
    def __init__(self):
        pass

    def _extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        
        g, x1, y1 = self._extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    def mod_inverse(self, a, m):
        g, x, y = self._extended_gcd(a, m)
        if g != 1:
            return 0
        
        return x % m

    def crt(self, remainders, moduli):
        num_congruences = len(moduli)
        if num_congruences == 0:
            return 0

        M = 1
        for m in moduli:
            M *= m

        result = 0
        for i in range(num_congruences):
            r_i = remainders[i]
            m_i = moduli[i]
            
            N_i = M // m_i
            
            x_i = self.mod_inverse(N_i, m_i)
            
            result += r_i * N_i * x_i
        
        return result % M

    def mod_exp(self, base, exponent, modulus):
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

    def is_quadratic_residue(self, a, p):
        if p == 2:
            return True
        
        a %= p
        if a == 0:
            return True
        
        exponent = (p - 1) // 2
        return self.mod_exp(a, exponent, p) == 1

    def order_mod(self, a, n):
        if self._extended_gcd(a, n)[0] != 1:
            return 0
        
        k = 1
        result = a % n
        while result != 1:
            result = (result * a) % n
            k += 1
            if k > n:
                return 0
        return k

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

    def is_fibonacci_prime(self, n):
        if not self._is_prime(n):
            return False
            
        a, b = 0, 1
        while b <= n:
            if b == n:
                return True
            a, b = b, a + b
            
        return False
