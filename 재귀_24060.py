update_list = []

def merge_sort(datas):
    if len(datas) == 1:
        return datas
    q = (len(datas)+1) // 2

    l = datas[:q]
    r = datas[q:]

    left_arr = merge_sort(l)
    right_arr = merge_sort(r)
    temp = merge(left_arr, right_arr)

    return temp


def merge(left_arr, right_arr):
    temp = []
    left_count = 0
    right_count = 0

    while left_count < len(left_arr) and right_count < len(right_arr):
        if left_arr[left_count] <= right_arr[right_count]:
            temp.append(left_arr[left_count])
            update_list.append(left_arr[left_count])
            left_count += 1
        else:
            temp.append(right_arr[right_count])
            update_list.append(right_arr[right_count])
            right_count += 1

    while left_count < len(left_arr):
        temp.append(left_arr[left_count])
        update_list.append(left_arr[left_count])
        left_count += 1

    while right_count < len(right_arr):
        temp.append(right_arr[right_count])
        update_list.append(right_arr[right_count])
        right_count += 1

    return temp


if __name__ == '__main__':
    base_line = input().split()

    length = int(base_line[0])
    k = int(base_line[1])
    datas = input().split()
    datas = [int(data) for data in datas]

    b = merge_sort(datas)
    print(f'result : {b}')
    print(update_list)

    if k > len(update_list):
        print(-1)
    else:
        print(update_list[k-1])
