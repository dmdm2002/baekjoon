def make_dict(n):
    d = {}
    for i in range(n):
        data = input()
        d[data] = str(i+1)

    return d


def mapping(voca_list, d):
    for voca in voca_list:
        print(d.get(voca))


n, m = map(int, input().split())
d = make_dict(n)
voca_list = [input() for _ in range(m)]
mapping(voca_list, d)
