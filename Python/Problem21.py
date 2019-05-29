import math

def get_sum_of_divisors(num):
    divisors = []
    i = 1
    while i <= math.sqrt(num):
        if num % i == 0:
            if i not in divisors:
                divisors.append(i)
                if i != int(num/i):
                    divisors.append(int(num/i))
        i += 1
    return sum(divisors) - num

def is_prime(num):
    if num == 1: return False
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0: return False
        i += 1
    return True

def find_all_amicable_numbers_under(maxValue):
    num = 1
    resultArray = []
    
    while num < maxValue:
        if is_prime(num):
            num += 1
            continue
        numDivisorsSum = get_sum_of_divisors(num)
        otherDivisorsSum = get_sum_of_divisors(numDivisorsSum)

        if numDivisorsSum != otherDivisorsSum and num == otherDivisorsSum:
            if num not in resultArray:
                resultArray.append(num)
                resultArray.append(numDivisorsSum)
        num += 1
    return sum(resultArray)

print(find_all_amicable_numbers_under(10000))