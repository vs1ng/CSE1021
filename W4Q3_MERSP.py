class MSP:
	def __init__(self, n: int)->None:
		self.n=n
	
	def __CheckIfNumberPrime(n: int)->bool:
        if n > 1:
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    #n isnt prime, hence not a prime-factor
                    pass
                else:
                    #yeah, n is prime
                    return True
        else:
            return False
    
	def isMerSennepRime(self):
		temp: int = pow(2,self.n)-1
		if self.__CheckIfNumberPrime(temp):
			#yeah, for a prime p, the 2^p-1 is also prime
			return True
		else:
			return False
	
		
