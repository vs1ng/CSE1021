class PRIMEPOWERS:
    def __init__(self, n: int) -> None:
        self.n = n
    def _get_unique_prime_factor_base(self) -> int:
        if self.n <= 1:
            return -1
        temp_n = self.n
        if temp_n % 2 == 0:
            unique_prime = 2
            while temp_n % 2 == 0:
                temp_n //= 2

            if temp_n == 1:
                return unique_prime
            return -1
        i = 3
        while i * i <= temp_n:
            if temp_n % i == 0:
                unique_prime = i
                while temp_n % unique_prime == 0:
                    temp_n //= unique_prime
                if temp_n == 1:
                    return unique_prime.
                return -1
            i += 2
         
        if temp_n > 1:
            return temp_n
        return -1
    def is_prime_power(self) -> bool:0.
        return self._get_unique_prime_factor_base() > 0
