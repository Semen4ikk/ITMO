with open("input.txt", "r") as inp:
    kirill = inp.readline().replace("\n", "")
    dima = inp.readline().replace("\n", "")


if (0 < len(kirill) <= 10000 and 0 < len(dima) <= 10000
    and len(kirill) == len(dima)):

    y = open("output.txt", "w")
    result = 0

    if kirill == dima:
        print(0)
        y.write(str(0))
    else:
        for i in range(0, len(kirill)):

            first_part = kirill[len(kirill) - i - 1:len(kirill)]
            second_part = kirill[0:len(kirill) - i - 1]
            sdvig = first_part + second_part

            if sdvig == dima:
                result += 1
                break

            result += 1

        if result != len(kirill):
            print(result)
            y.write(str(result))
        else:
            print(-1)
            y.write(str(-1))

    y.close()
