with open('input.txt', 'r') as file:
    days = int(file.readline())
    price = []
    for i in range(days):
        price.append(int(file.readline()))

def cafe(coupons_count, price):
    A = [[100000 for _ in range(coupons_count + 1)] for _ in range(coupons_count + 1)]
    A[0][0] = 0
    coupons = [0, 0]
    lunch = []
    for i in range(1, len(A)):
        for j in range(len(A[0]) - 1):
            if price[i - 1] <= 100:
                A[i][j] = min(A[i - 1][j] + price[i - 1], A[i - 1][j + 1])
            else:
                A[i][j] = min(A[i - 1][j - 1] + price[i - 1], A[i - 1][j + 1])
    minimum = min(A[coupons_count])
    for i in range(coupons_count):
        if minimum == A[coupons_count][i]:
            coupons[0] = i
    j = coupons[0]
    i = coupons_count
    coupons[1] = 0
    while i != 0 or j != 0:
        if price[i - 1] <= 100:
            if A[i - 1][j] + price[i - 1] <= A[i - 1][j + 1]:
                i -= 1
            else:
                lunch.append(i)
                i -= 1
                j += 1
                coupons[1] += 1
        else:
            if A[i - 1][j - 1] + price[i - 1] <= A[i - 1][j + 1]:
                i -= 1
                j -= 1
            else:
                lunch.append(i)
                i -= 1
                j += 1
                coupons[1] += 1
    return minimum, coupons, sorted(lunch)

with open('output.txt', 'w') as f:
    if 1 <= days <= 10 ** 2 and min(price) >= 0 and max(price) < 300:
        answ, coupons, coupon_days = cafe(days, price)
        f.write(str(answ) + '\n')
        for coupon in coupons:
            f.write(str(coupon) + ' ')
        for day in coupon_days:
            f.write('\n' + str(day))

