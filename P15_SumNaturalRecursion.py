#sum of n natural numbers using recursion

def sumNatural(n):
    if n == 1:
        return 1
    else:
        return n + sumNatural(n-1)
print(sumNatural(5))
