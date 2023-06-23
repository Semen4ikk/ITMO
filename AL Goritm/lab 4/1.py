def areEqual(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def FindPattern(t, p):
    result = []
    for i in range(len(t) - len(p) + 1):
        if areEqual(t[i:i + len(p)], p):
            result.append(str(i + 1))
    return result


with open('input.txt') as inp:
    p = inp.readline()[:-1]
    t = inp.readline()
with open('output.txt', 'w') as outp:
    result = FindPattern(t, p)
    outp.write(f'{len(result)}\n')
    outp.write(' '.join(result))
'''
Считываем подстроку p и ищем все ее вхождения в строку t наивным алгоритмом. Функция FindPattern проходится по всем 
подстрокам длины p основной строки, для каждой из них запускает фунцию areEqual, которая сравнивает  каждый символ двух 
строк. Если все символы совпадает, возвращает True и записывает индекс начала подстроки в основной строке.
'''

'''
aba
abaCaba

2
1 5
'''
