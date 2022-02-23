def IsPrime(num: int):
    num = abs(num)
    d = 2
    while d*d <= num:
        if num % d == 0:
            return False
        d += 1
    return True

def IsPrimeGaussianNumbers(re:int, im:int):
    if re!= 0 and im != 0 and IsPrime(re**2 + im**2):
        return True
    if (re == 0 or im == 0) and (abs(max(abs(re), abs(im))) % 4 == 3):
        return True
    return False
