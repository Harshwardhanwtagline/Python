def person_name(names_list):
    length_ele = [len(i) for i in names_list]
    all_names_len = [
        [j for j in names_list if len(j) == i] for i in sorted(set(length_ele))
    ]
    print("Names: {}\n".format(names_list))
    print("Name Lengths: {}\n".format(length_ele))
    print("The Three Most Frequent Name Length are: \n")
    for i in all_names_len[0:3]:
        print("{0} names of Length {1}: {2}".format(len(i), len(i[0]), i))
    
    print("The Three Least Frequent Name Length are: \n")
    for i in range(len(all_names_len)-1, 0, -1):
        print("{0} names of Length {1}: {2}".format(len(all_names_len[i]), len(all_names_len[i][0]), all_names_len[i]))



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