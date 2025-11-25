#!/bin/python3
class WEEK5:
    def __init__(self):
        pass

    def _sum_of_all_divisors(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        temp_n = n
        sum_div = 1
        
        # Factor 2
        p = 2
        exp = 0
        while temp_n % p == 0:
            exp += 1
            temp_n //= p
        
        if exp > 0:
            sum_div *= (p**(exp + 1) - 1) // (p - 1)

        # Factor odd primes
        p = 3
        while p * p <= temp_n:
            exp = 0
            while temp_n % p == 0:
                exp += 1
                temp_n //= p
            
            if exp > 0:
                sum_div *= (p**(exp + 1) - 1) // (p - 1)
                
            p += 2

        # Remainder is prime
        if temp_n > 1:
            sum_div *= (temp_n**2 - 1) // (temp_n - 1)
            
        return sum_div

    def aliquot_sum(self, n):
        if n <= 0:
            return 0
        return self._sum_of_all_divisors(n) - n

    def are_amicable(self, a, b):
        if a <= 1 or b <= 1:
            return False
            
        sum_a = self.aliquot_sum(a)
        sum_b = self.aliquot_sum(b)
        
        return sum_a == b and sum_b == a and a != b

    def multiplicative_persistence(self, n):
        n_str = str(n)
        if len(n_str) == 1:
            return 0
        
        persistence = 0
        current_num = n
        
        while current_num > 9:
            product = 1
            temp_num = current_num
            
            while temp_num > 0:
                digit = temp_num % 10
                product *= digit
                temp_num //= 10
            
            current_num = product
            persistence += 1
            
        return persistence

    def _count_divisors(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        total_divisors = 1
        temp_n = n
        
        # Factor out 2
        exponent = 0
        while temp_n % 2 == 0:
            exponent += 1
            temp_n //= 2
        
        if exponent > 0:
            total_divisors *= (exponent + 1)

        # Factor out odd numbers
        i = 3
        while i * i <= temp_n:
            exponent = 0
            while temp_n % i == 0:
                exponent += 1
                temp_n //= i
            
            if exponent > 0:
                total_divisors *= (exponent + 1)
                
            i += 2

        # Remainder is prime
        if temp_n > 1:
            total_divisors *= 2
            
        return total_divisors

    def is_highly_composite(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True

        current_divisors = self._count_divisors(n)
        
        for k in range(1, n):
            if self._count_divisors(k) >= current_divisors:
                return False
                
        return True

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
