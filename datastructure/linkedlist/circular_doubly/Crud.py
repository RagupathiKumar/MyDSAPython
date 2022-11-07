from Node import get_default


def read(head_node):

    if head_node is None:
        return

    current = head_node
    while current.next != head_node:
        print(current.value, end=" ")
        current = current.next
    else:
        print(current.value, end="\n")


if __name__ == "__main__":
    head = get_default()
    read(head)
