import functools


class Number:
    def __init__(self, numbers) -> None:
        self.numbers = numbers

    def get(self):
        return self.numbers

    def change_original_values(self, func):
        # Changing the value of list element on bases of lambda function
        return list(map(func, self.numbers))

    def filter_values(self, filter_func):
        # filtering the list element on bases of filter_func-lambda function
        return list(filter(filter_func, self.numbers))

    def compound_the_numbers(self, reduce_func):
        # compressing all the list element bases of reduce_func-lambda function
        return functools.reduce(reduce_func, self.numbers)

    def sort(self):
        # sorting list using sorted function
        return sorted(self.numbers)


if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
    n1 = Number(numbers)
    print("Numbers: ", n1.get())
    print("New values: ", n1.change_original_values(func=lambda x: x + x))
    print("Filtered values: ", n1.filter_values(filter_func=lambda x: x % 2 == 0))
    print("Compounded value: ", n1.compound_the_numbers(reduce_func=lambda x, y: x + y))
    print("Sorted List : ", n1.sort())
