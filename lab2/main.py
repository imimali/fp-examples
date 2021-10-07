def print_menu():
    pass


def read_command():
    return 0


def ui():
    while True:
        print_menu()
        command = read_command()
        if command == 0:
            print("Bye bye!")
            break


if __name__ == '__main__':
    ui()
