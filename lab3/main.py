from dataclasses import dataclass
import datetime


@dataclass
class Fruit:
    """
    Struct-like data structure to avoid keeping data in a list.
    """
    name: str
    color: str
    harvest_date: datetime.datetime


def print_menu():
    """
    Displays the choices the user has to the console
    :return:
    """
    print("1 - Add fruit")
    print("2 - Display all")
    print("3 - Delete all fruits older than a given date")
    print("4 - Undo")
    print("0 - Exit")


def read_command():
    """
    Reads the user choice from the console
    :return:
    """
    return int(input("Enter command: "))


def read_fruit():
    """
    Reads a fruit entity from the console
    :return:
    """
    name = input("Enter name: ")
    color = input("Enter color: ")
    harvest_d = read_date()
    return Fruit(name, color, harvest_d)


def read_date(prompt="Enter harvest date in YYYY/mm/dd format: "):
    """
    Reads and parses a date object from the console
    :param prompt:
    :return:
    """
    return datetime.datetime.strptime(input(prompt), "%Y/%m/%d")


def find_fruits_after_date(fruit_list, start_date):
    """
    Finds all fruits that were harvested after a given date
    :param fruit_list: list containing all fruits
    :param start_date: fruits have to be harvested before this
    :return:
    """
    return list(filter(lambda f: f.harvest_date > start_date, fruit_list))


def add_fruit(fruit_list, fruit):
    """
    Adds a fruit to the list of fruits
    :param fruit_list:
    :param fruit:
    :return:
    """
    fruit_list.append(fruit)


def display_list(fruit_list):
    """
    Display a list of fruits
    :param fruit_list:
    :return:
    """
    for fruit in fruit_list:
        print(fruit)


def save_for_undo(undo_list, fruit_list):
    """
    Saves the current application state for undo
    :param undo_list:
    :param fruit_list:
    :return:
    """
    undo_list.append(fruit_list)


# TODO add tests

def ui():
    fruits = [Fruit(f'mango{i}', f'red{i}', datetime.datetime(2021, 11, (i % 30) + 1)) for i in range(5)]
    undo_list = []
    while True:
        print_menu()
        command = read_command()

        if command == 1:
            save_for_undo(undo_list, fruits)
            fruit = read_fruit()
            add_fruit(fruits, fruit)

        if command == 2:
            display_list(fruits)

        if command == 3:
            save_for_undo(undo_list, fruits)
            bef_date = read_date("Enter date to filter by in YYYY/MM/dd format: ")
            fruits = find_fruits_after_date(fruits, bef_date)

        if command == 4:
            fruits = undo_list.pop()

        if command == 0:
            print("Bye bye!")
            break


if __name__ == '__main__':
    ui()
