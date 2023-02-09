def find_update_k(k, k_count, now_number, result_k):
    if k == k_count:
        result_k = now_number
        print(result_k)
        return result_k
    else:
        return result_k


def merge_sort(datas, k, k_count, result_k):
    if len(datas) < 2:
        return datas
    q = len(datas) // 2

    l = datas[:q]
    r = datas[q:]

    left_arr = merge_sort(l, k, k_count, result_k)
    right_arr = merge_sort(r, k, k_count, result_k)
    temp, k_count, result_k = merge(left_arr, right_arr, k, k_count, result_k)

    return temp


def merge(left_arr, right_arr, k, k_count, result_k):
    temp = []
    left_count = 0
    right_count = 0

    while left_count < len(left_arr) and right_count < len(right_arr):
        k_count += 1
        if left_arr[left_count] <= right_arr[right_count]:
            temp.append(left_arr[left_count])
            result_k = find_update_k(k, k_count, left_arr[left_count], result_k)

            left_count += 1
        else:
            temp.append(right_arr[right_count])
            result_k = find_update_k(k, k_count, right_arr[right_count], result_k)

            right_count += 1

    while left_count < len(left_arr):
        k_count += 1
        temp.append(left_arr[left_count])
        result_k = find_update_k(k, k_count, left_arr[left_count], result_k)

        left_count += 1

    while right_count < len(right_arr):
        k_count += 1
        temp.append(right_arr[right_count])
        result_k = find_update_k(k, k_count, right_arr[right_count], result_k)

        right_count += 1

    return temp, k_count, result_k

datas = []
length = int(input())
k = int(input())
k_count = 0
for _ in range(length):
    datas.append(int(input()))
print(datas)
# a = [4, 5, 1, 3, 2]
result_k = -1
b = merge_sort(datas, k, k_count, result_k)
