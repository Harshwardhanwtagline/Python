def numbers_operation(user_input, number_list):
    if user_input.lower() == "a":
        return "Length of the List : {}".format(len(number_list))
    elif user_input.lower() == "b":
        return "First 3 Numbers: {}".format(number_list[0:3])
    elif user_input.lower() == "c":
        odd_sum = sum([i for i in number_list if i % 2 != 0])
        return "Sum of odd Number: {}".format(odd_sum)
    elif user_input.lower() == "d":
        #In below line i have count the dulipcate form given list using dictionary comprehension.
        num_count = {num: number_list.count(num) for num in number_list}
        # duplicate_num is for finding max element occur in list using max function. 
        duplicate_num = max(zip(num_count.values(), num_count.keys()))
        return (
            "Number of duplicate numbers: {1} # ({1}, {0} repeats in the list)".format(
                duplicate_num[0], duplicate_num[1]
            )
        )
    elif user_input.lower() == "e":
        return "List without duplicate numbers: {}".format(list(set(number_list)))
    return "Invalid Input \nPlease Give Valid Input From(A, B, C, D, E)"


if __name__ == "__main__":
    user_input = str(input("Please Enter the Option : "))
    numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 2]
    print(numbers_operation(user_input, numbers))