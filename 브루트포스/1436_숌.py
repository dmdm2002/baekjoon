def mapping_666(series_number):
    if series_number == 1:
        return print(666)
    count = 1
    i = 666
    while True:
        i += 1

        i_str = str(i)
        if i_str.find('666') != -1:
            count += 1
            if count == series_number:
                print(i_str)
                break


if __name__ == '__main__':
    series_number = int(input())
    mapping_666(series_number)
