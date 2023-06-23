def compare(a, b):
    a = str(a)
    b = str(b)

    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return 1
        if a[i] > b[i]:
            return -1

    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
    return 0

def special_sort(array):
    if len(array) <= 1:
        return array

    state_element = array[0]

    left = []
    right = []
    middle = []

    for i in array:
        if compare(i, state_element) == 0:
            middle.append(i)
        if compare(i, state_element) == 1:
            right.append(i)
        if compare(i, state_element) == -1:
            left.append(i)

    left = special_sort(left)
    right = special_sort(right)

    return left + middle + right

f = open('input.txt')
n = list(map(int, f.readline().split()))

file_output = open('output.txt', 'w')
file_output.write(str(''.join(map(str, special_sort(n)))))
