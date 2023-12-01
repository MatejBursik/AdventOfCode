complete_sum = 0
with open("2023\\01\\input.txt","r") as f:
    for line in f:
        number = ""
        for character in line:
            if character.isdigit():
                number += character
                break
        for character in line[::-1]:
            if character.isdigit():
                number += character
                break

        complete_sum += int(number)

print("P1 sum is:",complete_sum)

import re

complete_sum = 0
pattern = r'(one|two|three|four|five|six|seven|eight|nine)'
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("2023\\01\\input.txt","r") as f:
    for line in f:
        str_num = ""
        number = ""
        for character in line:
            str_num += character
            matches = re.findall(pattern,str_num)
            if len(matches) > 0:
                number += str(numbers.index(matches[0])+1)
                break
            if character.isdigit():
                number += character
                break

        str_num = "" 
        for character in line[::-1]:
            str_num = character + str_num
            matches = re.findall(pattern,str_num)
            if len(matches) > 0:
                number += str(numbers.index(matches[0])+1)
                break
            if character.isdigit():
                number += character
                break

        complete_sum += int(number)

print("P2 sum is:",complete_sum)