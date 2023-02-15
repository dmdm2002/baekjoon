def make_dict(a_list):
    d = {}
    for a in (a_list):
        if d.get(a) is not None:
            d[a] = d.get(a) + 1
        else:
            d[a] = 1

    return d


def mapping(card_list, d):
    for card in card_list:
        temp = d.get(card)
        if temp is None:
            print(0, end=" ")
        else:
            print(temp, end=" ")


if __name__ == '__main__':
    a_count = int(input())
    a_list = list(map(int, input().split()))

    b_count = int(input())
    b_list = list(map(int, input().split()))

    d = make_dict(a_list)
    mapping(b_list, d)
