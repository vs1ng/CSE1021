def is_harshad(n: int) -> bool:
    s: int = 0
    for i in str(n):
        s+=int(i)
    if n%s==0:
        return True
    else:
        return False
