def count_substring(string, substring):
    # Using list comprehension and slicing, i have count the occcurence of substring in string. and then i have append 1 in list,
    # after the i have sum all using sum function
    count = sum(
        [
            1
            for index in range(0, len(string))
            if string[index : len(substring) + index] == substring
        ]
    )
    return count

if __name__ == "__main__":
    string = "PQRQRQRQ"
    substring = "QRQ"
    print(count_substring(string, substring))
