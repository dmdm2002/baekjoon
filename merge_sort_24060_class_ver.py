class MergeSort:
    def __init__(self, k):
        self.k = k
        self.k_count = 0
        self.k_result = -1

    def find_update_k(self, now_number):
        if int(self.k) == self.k_count:
            self.k_result = now_number

    def merge_sort(self, data):
        if len(data) == 1:
            return data
        q = (len(data) + 1) // 2

        l = data[:q]
        r = data[q:]

        left_arr = self.merge_sort(l)
        right_arr = self.merge_sort(r)
        temp = self.merge(left_arr, right_arr)

        return temp

    def merge(self, left_arr, right_arr):
        temp = []
        left_count = 0
        right_count = 0

        while left_count < len(left_arr) and right_count < len(right_arr):
            self.k_count += 1
            if left_arr[left_count] <= right_arr[right_count]:
                temp.append(left_arr[left_count])
                self.find_update_k(left_arr[left_count])

                left_count += 1
            else:
                temp.append(right_arr[right_count])
                self.find_update_k(right_arr[right_count])

                right_count += 1

        while left_count < len(left_arr):
            self.k_count += 1
            temp.append(left_arr[left_count])
            self.find_update_k(left_arr[left_count])

            left_count += 1

        while right_count < len(right_arr):
            self.k_count += 1
            temp.append(right_arr[right_count])
            self.find_update_k(right_arr[right_count])

            right_count += 1

        return temp


if __name__ == '__main__':
    base_line = input().split()

    length = int(base_line[0])
    k = int(base_line[1])
    datas = input().split()
    datas = [int(data) for data in datas]

    merge_sort = MergeSort(k)
    result_arr = merge_sort.merge_sort(datas)
    print(merge_sort.k_result)
