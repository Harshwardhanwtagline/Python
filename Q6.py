def count_substring(string, substring):
    count = 0
    for i in range(0,len(string)):
        if string[i:len(substring)+i] == substring:
            count += 1
    return count


if __name__ == "__main__":
    string = "PQRQRQRQ"
    substring = "QRQ"
    print(count_substring(string, substring))