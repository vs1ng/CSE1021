#!/bin/python3
class WEEK8:
    def __init__(self):
        pass

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

    def is_prime_miller_rabin(self, n, k):
        if n <= 1: return False
        if n == 2 or n == 3: return True
        if n % 2 == 0: return False

        r = n - 1
        s = 0
        while r % 2 == 0:
            r //= 2
            s += 1

        for _ in range(k):
            a = (_ * 2 + 2) % (n - 2) + 2
            if a == 0: a = 2
            
            x = self._mod_exp(a, r, n)
            
            if x == 1 or x == n - 1:
                continue

            for _ in range(s - 1):
                x = self._mod_exp(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        
        return True

    def pollard_rho(self, n):
        if n % 2 == 0: return 2
        
        x = 2
        y = 2
        d = 1
        
        def g(val, num):
            return (val * val + 1) % num

        while d == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            d = self._gcd(abs(x - y), n)

            if d == n:
                x = x + 1
                y = x
                d = 1

        return d

    def zeta_approx(self, s, terms):
        if s <= 1 or terms <= 0:
            return 0.0

        zeta_sum = 0.0
        
        for n in range(1, terms + 1):
            
            def float_power(base, exp):
                if exp == 0:
                    return 1.0
                
                result = 1.0
                is_negative = exp < 0
                exp = abs(exp)
                
                for _ in range(exp):
                    result *= base
                    
                if is_negative:
                    return 1.0 / result
                return result

            n_to_s = float_power(float(n), float(s))
            if n_to_s != 0:
                zeta_sum += 1.0 / n_to_s
            
        return zeta_sum

    def partition_function(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1
            
        
        partitions = bytearray([1])
        
        for i in range(1, n + 1):
            p_i = 0
            k = 1
            while True:
                
                g1 = k * (3 * k - 1) // 2
                
                g2 = k * (3 * k + 1) // 2
                
                sign = (-1)**(k - 1)
                
                
                if i - g1 >= 0:
                    p_i += sign * partitions[i - g1]
                else:
                    break
                
                
                if i - g2 >= 0:
                    p_i += sign * partitions[i - g2]
                else:
                    break

                k += 1
            
            
            partitions.append(p_i % 256)
            
        return int(partitions[n])
