import copy

with open('input.txt') as file:
    length_of_number = int(file.readline())

def find_value_of_numbers(length_of_number):
    previos = [4, 2, 1, 0]
    current = [0 for _ in range(4)]

    if length_of_number > 1:
        for i in range(length_of_number - 1):
            current[0] += previos[1] * 2 + previos[2] * 2
            current[1] += previos[0] + previos[3] * 2
            current[2] += previos[0]
            current[3] += previos[1]
            previos = copy.copy(current)
            current = [0 for _ in range(4)]

        return sum(previos)
    else:
        return 8

result = find_value_of_numbers(length_of_number)

f = open('output.txt', 'w')
f.write(str(result))
