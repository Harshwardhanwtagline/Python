def list_sort(num_list):
    #using bubble sort algorithm i have sorted the list
    for i in range(0, len(num_list) - 1):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


if __name__ == "__main__":
    num_list = [2, 5, 6, 1, 3, 8, 9, 10]
    print("Sorted List is : {}".format(list_sort(num_list)))