n_origin = int(input())
n = n_origin
count = 0

while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    n = (b*10) + c
    count += 1

    if (n==n_origin):
        break

print(count)
