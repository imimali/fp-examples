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
    return []


def test_find_odd():
    assert find_odd([]) == []


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
    ui()
