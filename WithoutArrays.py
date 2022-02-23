def IsPrime(num: int):
    num = abs(num)
    d = 2
    while d*d <= num:
        if num % d == 0:
            return False
        d += 1
    return True