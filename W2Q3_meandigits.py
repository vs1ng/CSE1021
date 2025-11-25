def mean_of_digits(n: int) -> float:
    digits: bytearray = bytearray(len(str(n)))
    index=0
    for digit in str(n):
        digits[index]=int(digit)
        index+=1
    avg: float = sum(digits)/len(str(n)) 
    return avg
