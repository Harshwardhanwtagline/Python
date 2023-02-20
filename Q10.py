def diamond_pattern(n):

    #i have iterated over loop to print the pattern, i have print _ in odd-number and * in even number occurence.
    for i in range(1, n + 1, 2):
        print('*' * int((n - i) / 2) + '-' * i + '*' * int((n - i) / 2))

    #i have iterated over loop to print the pattern, i have print * in odd-number and _ in even number occurence.
    for i in range(n - 2, 0, -2):
        print('*' * int((n - i) / 2) + '_' * i + '*' * int((n - i) / 2))

def diamond_mid_pattern(n):

    #i have iterated over loop to print the pattern, i have print * in odd-number and _ in even number occurence.
    for i in range(1, n + 1, 2):
        print('_' * int((n - i) / 2) + '*' * i + '_' * int((n - i) / 2))
    
    #i have iterated over loop to print the pattern, i have print _ in odd-number and * in even number occurence.
    for i in range(n - 2, 0, -2):
        print('_' * int((n - i) / 2) + '*' * i + '_' * int((n - i) / 2))

def triangle_pattern(n):

    #i have iterated over loop to print the pattern, but over here i have print _ in the center of triangle using condition.
    for i in range(1, n+1):
        for j in range(1, i + 1):
            if j==1 or j==i or i==n:
                print("*", end="")
            else:
                print("_", end="")
        print("\r")


def square_pattern(n):

    #i have iterated over loop to print the pattern, but over here i have print _ in the center of square using condition.
    for i in range(0,n+1):
        for j in range(1, n+1):
            if i==1 or j==1 or i==n or j==n:
                print("_", end=" ")
            else:
                print("*", end=" ")
        print("\r")

def number_triangle_pattern(n):

    #i have iterated over loop to print the number pattern, num variable is increases in every iteration and printed 
    num = 1
    for i in range(0, n+1):
        for j in range(0,i):
            print(num, end=" ")
            num = num+1
        print("\r")


if __name__ == "__main__":
    n = 5
    diamond_pattern(n)
    diamond_mid_pattern(n)
    triangle_pattern(n)
    square_pattern(n)
    number_triangle_pattern(n)

    
