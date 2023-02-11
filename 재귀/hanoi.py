def hanoi(N, from_pos, to_pos, aux_pos):
    if N == 1:
        count_list.append([from_pos, to_pos])
        return

    hanoi(N - 1, from_pos, aux_pos, to_pos)
    count_list.append([from_pos, to_pos])
    hanoi(N - 1, aux_pos, to_pos, from_pos)


if __name__ == '__main__':
    N = int(input())
    count_list = []
    hanoi(N, 1, 3, 2)
    print(len(count_list))
    for changing in count_list:
        print(f'{changing[0]} {changing[1]}')
