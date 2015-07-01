from decimal import *
"""
    Enter a number n;
    Then generate PI;
"""
getcontext().prec = 50

def sumation(n,term):
    total,k = Decimal(0.0),1
    while k <= n:
        total += term(k)
        k += 1
    return total

def PI_term(k):
    return Decimal(8)/((4*k-3)*(4*k-1))

def PI_sum(n):
    return sumation(n,PI_term)

def main():
    n = int(input("Input length of PI: "))
    while n not in range(1,50):
        n = int(input("Please input a number in [1,50]: "))
    PI = PI_sum(10000)
    s = str(PI)
    return print(s[:n])

if __name__ =='__main__':
    main()

