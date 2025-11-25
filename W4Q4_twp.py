#!/bin/python3
class PRIMEPair:
    def __init__(self):
        pass

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

    def twin_primes(self, limit):
        twin_primes_list = bytearray()
        
        n = 2
        while n + 2 <= limit:
            if self._is_prime(n) and self._is_prime(n + 2):
                if n > 255 or n + 2 > 255:
                    return twin_primes_list
                twin_primes_list.append(n)
                twin_primes_list.append(n + 2)
            n += 1
            
        return twin_primes_list
