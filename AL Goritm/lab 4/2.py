with open('input.txt') as inp:
    word = inp.readline().split(' ')
    word = ''.join(word)
alph, q = dict(), dict()

for i in range(len(word)):
    letter = word[i]
    try:
        alph[letter] += 1
    except:
        alph[letter] = 0
        alph[letter] += 1

c = 0
for key in alph:
    copy = word
    if alph[key] >= 2:
        c += 1
        q[key] = []
        for i in range(len(word)):
            if word[i] == key:
                q[key].append(i)
result = 0

for letter in q:
    coef = len(q[letter]) - 1
    for i in reversed(range(len(q[letter]))):
        result += q[letter][i] * coef
        coef -= 2
    result -= (len(q[letter]) - 1) * len(q[letter]) // 2

with open('output.txt', 'w') as outp:
    outp.write(str(result))



'''
Считываем строку и проходимся по ней, записывая в  словарь alph количество символов в строке, а в словарь q записываем 
индексы этих символов, если их больше 1. Затем считываем количество возможных вариантов, считая количество символов 
между двумя повторяющимися для каждого символа.
'''
