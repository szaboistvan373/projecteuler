def get_sum_of_number_name_letters_until(range):
    i = 1
    sum = 0

    while i <= range:
        sum += get_char_count(get_name_of_number(i))
        i += 1
    return sum

def get_name_of_number(number):
   length = len(str(number))

   if str(number) == '0' or str(number) == '00':
       return ""

   if length == 1 or int(number) <= 12:
       return get_name_of_small_number(number)

   if int(number) < 20:
       prefix = {
           3: 'thir',
           4: 'four',
           5: 'fif',
           6: 'six',
           7: 'seven',
           8: 'eigh',
           9: 'nine',
       }[int(str(number)[1])]

       return prefix + "teen"

   if length == 4:
       return "one thousand"

   output = ""

   if length == 3:
       output += get_name_of_small_number(str(number)[0]) + " hundred"

       secondPart = get_name_of_number(str(number)[1] + str(number)[2])

       if secondPart != "":
           output += " and " + secondPart
       else:
           output += " " + secondPart

       return output

   output = get_name_of_decimal(str(number)[0]) + " " + get_name_of_number(str(number)[1])

   return output

def get_char_count(textWithSpaces):
    return len(str(textWithSpaces).replace(" ", ""))

def get_name_of_small_number(number):
    return {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
    }[int(number)]

def get_name_of_decimal(decimalNumber):
    return {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }[int(decimalNumber)]


print(get_name_of_number(12))

print(get_sum_of_number_name_letters_until(1000))

print(get_name_of_number(420))