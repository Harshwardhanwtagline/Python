def list_sort(list_1):
    for i in range(0, len(list_1) - 1):
        for j in range(0, len(list_1) - i - 1):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
    return list_1


if __name__ == "__main__":
    list_1 = [2, 5, 6, 1, 3, 8, 9, 10]
    print("Sorted List is : {}".format(list_sort(list_1)))