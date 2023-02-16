import time
def person_name(names_list):
    #In Below Line i have calculate lenght of every word in list using lenght-function
    length_element = [len(name) for name in names_list]
    """
    First i have use set contructor to remove duplicate element in list and after then i have use sorted to sort the element,
    after then on bases of length_element list i have separated the names form names_list.
    """
    all_names_length = [
        [name for name in names_list if len(name) == length] for length in sorted(set(length_element))
    ]
    print("Names: {}\n".format(names_list), "\nName Lengths: {}\n".format(length_element),"\nThe Three Most Frequent Name Length are: \n")
    for i in all_names_length[0:3]:
        print("{0} names of Length {1}: {2}".format(len(i), len(i[0]), i))
    
    print("The Three Least Frequent Name Length are: \n")
    for i in range(len(all_names_length)-1, 0, -1):
        print("{0} names of Length {1}: {2}".format(len(all_names_length[i]), len(all_names_length[i][0]), all_names_length[i]))



if __name__ == "__main__":
    names = [
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        "Wilson",
        "Moore",
        "Taylor",
        "Anderson",
        "Thomas",
        "Jackson",
        "White",
    ]
    person_name(names)