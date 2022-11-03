from Node import get_default
from Crud import read, add_values, remove_value, get_length


def menu_card():
    print("\n" + ("~" * 5) + " MAIN MENU :: Linked List " + ("~" * 5))
    print("1:READ 2:INSERT 3:DELETE 4:LENGTH 5:EXIT")
    try:
        return int(input("OPTION :: "))
    except ValueError:
        return -1


if __name__ == "__main__":

    head = get_default()

    while True:
        option = menu_card()
        match option:
            case 1:
                read(head)
            case 2:
                try:
                    val = int(input("Enter value :: "))
                    add_values(head, val)
                    print("Insertion successful")
                except ValueError:
                    print("Incorrect value, Try again.")
            case 3:
                try:
                    val = int(input("Enter value :: "))
                    head = remove_value(head, val)
                    print("Deletion successful")
                except ValueError:
                    print("Incorrect value, Try again.")
            case 4:
                print("Length is " + str(get_length(head)))
            case default:
                print("See you later!")
                break




