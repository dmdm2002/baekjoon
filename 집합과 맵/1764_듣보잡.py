def mapping(n_peoples, m_peoples):
    mapping_list = list(set(n_peoples) & set(m_peoples))
    mapping_list.sort()
    print(len(mapping_list))
    for name in mapping_list:
        print(name)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    n_peoples = [input() for _ in range(n)]
    m_peoples = [input() for _ in range(m)]

    mapping(n_peoples, m_peoples)
