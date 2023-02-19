def make_dict(backbone_list):
    d = {}
    for value in (backbone_list):
        d[value] = True

    return d

# 사전순으로 sorting이 필요하다.
def mapping(a, d):
    sub_set_count = 0
    for number in a:
        search_result = d.get(number)
        if search_result is None:
            sub_set_count += 1

    return sub_set_count


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    d = make_dict(a_list)
    a_sub_set_count = mapping(b_list, d)

    d = make_dict(b_list)
    b_sub_set_count = mapping(a_list, d)

    print(a_sub_set_count + b_sub_set_count)
