if __name__ == '__main__':
    text = input()
    _set = set()

    for i in range(len(text)):
        for j in range(i, len(text)):
            _set.add(text[i:j + 1])

    print(len(_set))
