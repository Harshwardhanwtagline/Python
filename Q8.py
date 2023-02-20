def list_sort(num_list):
    # using bubble sort algorithm i have sorted the list
    for index in range(0, len(num_list) - 1):
        for cur_index in range(0, len(num_list) - index - 1):
            if num_list[cur_index] > num_list[cur_index + 1]:
                num_list[cur_index], num_list[cur_index + 1] = (
                    num_list[cur_index + 1],
                    num_list[cur_index],
                )
    return num_list


if __name__ == "__main__":
    num_list = [2, 5, 6, 1, 3, 8, 9, 10]
    print("Sorted List is : {}".format(list_sort(num_list)))
