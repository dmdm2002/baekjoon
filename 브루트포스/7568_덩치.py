def compare_weight(a_info, b_info, rank, i):
    if a_info[0] < b_info[0] and a_info[1] < b_info[1]:
        rank[i] += 1


if __name__ == '__main__':
    number_of_people = int(input())
    student_list = []
    rank = [1] * number_of_people

    for _ in range(number_of_people):
        weight, height = map(int, input().split())
        student_list.append((weight, height))

    for i in range(number_of_people):
        original_temp = student_list.copy()
        temp_std_1 = original_temp.pop(i)
        temp_std_2 = original_temp.copy()

        for j in range(len(temp_std_2)):
            compare_weight(temp_std_1, temp_std_2[j], rank, i)

    for i in rank:
        print(i, end=" ")
