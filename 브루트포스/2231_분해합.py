def encoding(n):
    if n > 100:
        start = n - 100

    else:
        start = 0

    for i in range(start, n):
        temp = i
        # print(temp)
        for j in str(i):
            temp += int(j)

        if temp == n:
            return print(i)

    return print(0)


if __name__ == '__main__':
    n = int(input())
    encoding(n)
