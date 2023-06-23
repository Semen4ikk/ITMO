with open('input.txt') as file:
    inf_from_file = int(file.readline())

def find_max_det(number):
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            return i

def happy_kids(value_of_candies):
    value_of_pairs = find_max_det(value_of_candies)
    k = value_of_pairs
    candies = []

    while value_of_pairs != 0:
        candies.append(value_of_pairs)
        value_of_pairs -= 1

    return k, candies


k, candies = happy_kids(inf_from_file)
print(k, candies)
f = open('output.txt', 'w')
f.write(str(k))
f.write()
