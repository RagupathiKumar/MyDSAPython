from Node import Node, get_default


def read(node):
    while node is not None:
        print(node.value, end=" ")
        node = node.next
    print("")


def add(head_node, *nodes):
    for node in nodes:

        if head_node is None:
            head_node = node
            continue

        last_node = head_node
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = node


def add_values(head_node, *values):
    for value in values:
        add(head_node, Node(value))


def remove(head_node):

    previous = None
    curr = head_node
    while curr is not None:

        if curr.next is None:
            if previous is None:
                head_node = None
            else:
                previous.next = None
            break
        else:
            previous = curr
            curr = curr.next

    return head_node


def remove_value(head_node, *values):
    for value in values:

        previous = None
        curr = head_node

        while curr is not None:

            if curr.value == value:
                if previous is None:
                    head_node = curr.next
                else:
                    previous.next = curr.next
                break
            else:
                previous = curr
                curr = curr.next

        return head_node


def get_length(head_node):
    length = 0
    curr = head_node
    while curr is not None:
        length += 1
        curr = curr.next
    return length


if __name__ == '__main__':
    head = get_default()
    read(head)

    add(head, Node(4), Node(6), Node(7), Node(8))
    read(head)

    add_values(head, 9, 10)
    read(head)

    head = remove(head)
    read(head)

    head = remove_value(head, 1)
    read(head)

    print(get_length(head))
