def is_palindrome(n: int) -> bool:
    if n == int(str(n)[::-1]): 
        return True
    else:
        return False
