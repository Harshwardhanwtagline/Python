def fib(n):
    def fibonacci(position, result_dict):
        #Checking the position already exists into result_dict, if exists the returning it.
        if position in result_dict:
            return result_dict[position]
        
        # I have stored the result into result variable after addition of two number
        result = fibonacci(position - 1, result_dict) + fibonacci(position - 2, result_dict)
        #after getting result adding into result_dict
        result_dict[position] = result
        return result

    result_dict = {1: 1, 2: 1}
    return fibonacci(position, result_dict)


def sum_list(num):
    # I have use pop method to remove and then added and condition is for if num is empty then add zero.
    return num.pop() + sum_list(num) if num else 0


if __name__ == "__main__":
    position = int(input("Enter the Position To Find the Number: "))
    numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
    print("The Fibonacci position Number: {}".format(fib(position)),"\nSum of list is : {}".format(sum_list(numbers)))