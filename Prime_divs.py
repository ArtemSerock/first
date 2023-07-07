import math
def Prime_div(num):
    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        for i in range(3, math.ceil(n ** 0.5), 2):
            if n % i == 0:
                return False
        return True
    result = []
    for j in range(2, num+1):
        if num % j == 0 and is_prime(j):
            result.append(j)
    return result

