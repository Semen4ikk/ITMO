with open("input.txt", "r") as inp:
    str1 = inp.readline().split()
str2 = str1[0]
len_of_w = 0
for i in range(len(str2)):
    lett = str2[i] #перебираем буквы и сравниваем_с_каждой
    for j in range(i, len(str2)):
        if lett == str2[j]:
            len_of_w2 = j - i
            if len_of_w2 > len_of_w:
                len_of_w = len_of_w2

#print(len_of_w)

with open("output.txt", "w") as outp:
    outp.write(str(len_of_w) + "\n")


