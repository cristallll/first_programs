# Shuffling the list of ordered integer numbers, and checking the effectiveness
# of this process, counting how many items are left in their original positions.

from random import randint


def start(numbers: int):
    '''
    Method starts a shuffling program.
    :param numbers: Integer numbers, starts with 0
    :return: Calls a generating method
    '''
    generate_list_of_integer_numbers(numbers)


def generate_list_of_integer_numbers(numbers: int):
    '''
    Method generates ordered list of integer numbers.
    :param numbers: Integer numbers
    :return: Print initial list of ordered numbers, next call a shuffling method
    '''
    list_ = []
    for number in range(numbers):
        list_.append(number)
    print(f"Ordered list:  {list_}")
    shuffle_list_of_numbers(list_, numbers)


def shuffle_list_of_numbers(list_: list, numbers: int):
    '''
    Method shuffles ordered list of integer numbers and generated random integer numbers.
    :param list_: Ordered list of integer numbers
    :param numbers: Integer numbers
    :return: Print shuffled list, next call a caunting method
    '''
    for number in range(numbers):
        rand = randint(0, numbers - 1)
        list_[number], list_[rand] = list_[rand], list_[number]  # The next element
        # of the list turns its place with random element.
    print(f"Shuffled list: {list_}")
    count_not_shuffled_numbers(list_, numbers)


def count_not_shuffled_numbers(list_: list, numbers: int):
    '''
    Method counts not shuffled numbers, remained in their original position.
    :param list_: Shuffled list of integer numbers
    :param numbers: Integer numbers
    :return: Print not shuffled numbers, and number of such elements in their original position
    '''
    count = 0
    print("Not shuffled numbers: ", end="")
    for number in range(numbers):
        if list_[number] == number:  # Checking if values of elements of the shuffled
            # list are equal to their indexes, so they are not shuffled
            count += 1
            print(f"{list_[number]}, ", end="")  # Enumeration of numbers that
            # are still on their own original positions (they are not shuffled)
    print(f"\nNumber of elements on their origin positions is {count}")


if __name__ == '__main__':
    start(10)
