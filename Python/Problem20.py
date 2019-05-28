def get_factorial_of(n):
    i = 1
    product = 1
    while i <= n:
        product *= i
        i += 1
    return product

factorial_result = get_factorial_of(100)

sum_of_numbers = 0

for char in str(factorial_result):
    sum_of_numbers += int(char)

print(sum_of_numbers)