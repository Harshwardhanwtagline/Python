def fib(n):
    def fibonacci(n, m):
        if n in m:
            return m[n]

        result = fibonacci(n - 1, m) + fibonacci(n - 2, m)
        m[n] = result
        return result

    m = {1: 1, 2: 1}
    return fibonacci(n, m)


def sum_list(num):
    return num.pop() + sum_list(num) if num else 0


if __name__ == "__main__":
    n = int(input("Enter the Number: "))
    numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
    print("The Fibonacci position Number: {}".format(fib(n)))
    print("Sum of list is : {}".format(sum_list(numbers)))