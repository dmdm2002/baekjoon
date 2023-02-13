def binary_search(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1

        elif key > lst[mid]:
            low = mid + 1

        else:
            return 1

    return 0


if __name__ == '__main__':
    a_count = int(input())
    a_list = list(map(int, input().split()))
    a_list = sorted(a_list)

    b_count = int(input())
    b_list = list(map(int, input().split()))

    for b_val in b_list:
        answer = binary_search(a_list, b_val)
        print(answer, end=' ')
