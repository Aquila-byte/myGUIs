a = 1
b = int(a + 1)
c = int(b + 1)
while True:
    if a ** 2 + b**2 == c**2:
        print(a, b, c)
        break
    a += 1
    b += 1
    c += 1

while True:
    if a ** 2 + b ** 2 + c ** 2 == 1000:
        print(a, b, c)
        break
    a += 1
    b += 1
    c += 1
