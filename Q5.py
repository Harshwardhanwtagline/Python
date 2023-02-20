from itertools import permutations


def list_sum(num_list, user_input):
    # I have use itertools-library to get permutations of different element.
    permutations_list = list(permutations(num_list, 2))
    # i have separated the combination of list, who's sum is equal to user_input and convert into list.
    sum_list = [list(ele) for ele in set(permutations_list) if sum(ele) == user_input]
    # after then i have filter the dulipcate on base of condition.
    result = list(filter(lambda x: x[0] < x[1], sum_list))
    return result

if __name__ == "__main__":
    num_list = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
    user_input = int(input("Enter the Number: "))
    print(list_sum(num_list, user_input))
