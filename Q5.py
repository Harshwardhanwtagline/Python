from itertools import permutations


def list_sum(num, n):
    list_1 = list(permutations(num, 2))
    list_2 = [i for i in set(list_1) if sum(i) == n]
    result = [list(i) for i in list_2 if i[0] < i[1]]
    return result


if __name__ == "__main__":
    num = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
    n = int(input("Enter the Number: "))
    print(list_sum(num, n))