def like_black_jack(m: int, now_answer, card_list: list):
    if len(card_list) < 3:
        return now_answer

    std_1 = card_list.pop(0)

    sampling_card_list = card_list.copy()
    now_answer = check_sample_sum(m, now_answer, std_1, sampling_card_list)

    return like_black_jack(m, now_answer, card_list)


def check_sample_sum(m, now_answer, std_1, sampling_card_list):
    for i in range(len(sampling_card_list)):
        for j in range(len(sampling_card_list)):
            if j + 1 < len(sampling_card_list) and i != j+1:
                sum = std_1 + sampling_card_list[i] + sampling_card_list[j+1]
                temp = m - sum
                if (temp < (m - now_answer)) and (temp >= 0):
                    now_answer = sum

    return now_answer


if __name__ == '__main__':
    length_and_m = input().split()

    length = int(length_and_m[0])
    m = int(length_and_m[1])

    card_list = input().split()
    cards = [int(card_list[i]) for i in range(length)]

    answer = like_black_jack(m, 0, cards)
    print(answer)
