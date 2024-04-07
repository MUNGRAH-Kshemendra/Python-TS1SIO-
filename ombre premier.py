def est_divisible (a,b):
    if a % b == 0:
        return True
    else :
        return False
print (est_divisible(30,5))
print (est_divisible(75,5))
print (est_divisible(6,5))


def est_premier(a):
    racine = int(a**0,5)
    for d in range(2,racine + 1):
        if est_divisible(a,d):
            return False
    return True


for k in range(21):
    if est_premier(a):
        print(a)