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


def ui():
    while True:
        print_menu()
        command = read_command()
        if command == 0:
            print("Bye bye!")
            break


if __name__ == '__main__':
    ui()
