def diamond_pattern(n):
    for i in range(1, n + 1, 2):
        print('* ' * int((n - i) / 2) + '- ' * i + '* ' * int((n - i) / 2))
    for i in range(n - 2, 0, -2):
        print('* ' * int((n - i) / 2) + '_ ' * i + '* ' * int((n - i) / 2))

def diamond_mid_pattern(n):
    for i in range(1, n + 1, 2):
        print('_ ' * int((n - i) / 2) + '* ' * i + '_ ' * int((n - i) / 2))
    for i in range(n - 2, 0, -2):
        print('_ ' * int((n - i) / 2) + '* ' * i + '_ ' * int((n - i) / 2))

def triangle_pattern(n):
    for i in range(0, n+1):
        for j in range(0, i):
            if (i==3 and j==1) or (i==4 and (j==1 or j==2)):
                print("_", end=" ")
            else:
                print("*", end=" ")
        print("\r")

def square_pattern(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i==1 or j==1 or i==5 or j==5:
                print("*", end=" ")
            else:
                print("_", end=" ")
        print("\r")

def number_triangle_pattern(n):
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