#!/bin/python3

class PrimeFactors:
    def __init__(self,n: int)->None:
        self.n=n

    def __CheckIfNumberPrime(self)->bool:
        if self.n > 1:
            for i in range(2,int(self.n**0.5)+1):
                if self.n%i==0:
                    #n isnt prime, hence not a prime-factor
                    pass
                else:
                    #yeah, n is prime
                    return True
        else:
            return False
    
    def PF(self)->bool:
        factors: bytearray = bytearray()
        for i in range(1,self.n):
            if self.n%i==0:
                if self.__CheckIfNumberPrime():
                    factors.append(i)
                else:
                    pass
            pass
        return factors

