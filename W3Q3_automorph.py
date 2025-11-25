def is_automorphic(n: int) -> bool:
    if str(n**2)[-len(str(n)):] == str(n):
        return True
    else:
        return False
