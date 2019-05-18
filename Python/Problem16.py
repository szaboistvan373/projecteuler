import math


def GetSumOfDigits(number):
    number = str(number)
    sum = 0

    for i in range(len(number)):
        sum += int(number[i])
    return sum

number = int(math.pow(2,1000))

sumOfDigits = GetSumOfDigits(number)

print(sumOfDigits)