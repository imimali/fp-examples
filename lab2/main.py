def print_menu():
    """
    Displays the choices the user has to the console
    :return:
    """
    print("1 - Find all odd elements")
    print("0 - Exit")


def read_command():
    """
    Reads the user choice from the console
    :return:
    """
    return int(input("Enter command: "))


def find_odd(elements):
    """
    Finds all elments that are odd in a list of numbers
    :param elements: list of integer numbers
    :return: a list with all odd numbers from elements
    """
    result = []
    for elem in elements:
        if elem % 2 == 1:
            result.append(elem)
    return result


def test_find_odd():
    assert find_odd([]) == []
    assert find_odd([1, 3]) == [1, 3]
    assert find_odd([1, 2, 3]) == [1, 3]
    assert find_odd([2, 4, 6, 8]) == []
    assert find_odd([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    print("Tests passed :)")


def ui():
    numbers = [1, 2, 5, 8, 10, 45, 9, 2]
    while True:
        print_menu()
        command = read_command()
        if command == 1:
            odd_numbers = find_odd(numbers)
            print("Odd numbers are", odd_numbers)
        if command == 0:
            print("Bye bye!")
            break


if __name__ == '__main__':
    test_find_odd()
    ui()
