def digital_sum(n: int) -> int:
    s: int = 0
    for i in str(n):
        s+=int(i)
    return s 
