from itertools import permutations


def list_sum(num_list, user_input):
    permutations_list = list(permutations(num_list, 2))
    sum_list = [list(_) for _ in set(permutations_list) if sum(_) == user_input]
    result = list(filter(lambda x: x[0]< x[1] , sum_list))
    return result


if __name__ == "__main__":
    num_list = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
    user_input = int(input("Enter the Number: "))
    print(list_sum(num_list, user_input))