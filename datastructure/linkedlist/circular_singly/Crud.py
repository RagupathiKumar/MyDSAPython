from Node import get_default, Node


def read(head_node):
    current = head_node
    while current.next != head_node:
        print(current.value, end=" ")
        current = current.next
    else:
        print(current.value, end="\n")


def add_first(head_node, value):
    node = Node(value)

    if head_node is None:
        node.next = node
        return node

    last = head_node
    while last.next != head_node:
        last = last.next

    last.next = node
    node.next = head_node
    return node


def add_last(head_node, value):
    node = Node(value)

    if head_node is None:
        node.next = node
        return node

    last = head_node
    while last.next != head_node:
        last = last.next

    last.next = node
    node.next = head_node
    return head_node


def remove_first(head_node):
    if head_node is None or head_node.next == head_node:
        return None

    last = head_node
    while last.next != head_node:
        last = last.next

    last.next = head_node.next
    return head_node.next


def remove_last(head_node):
    if head_node is None or head_node.next == head_node:
        return None

    second_last = None
    last = head_node
    while last.next != head_node:
        second_last = last
        last = last.next

    second_last.next = last.next
    return head_node


if __name__ == "__main__":
    head = get_default()
    read(head)

    head = add_first(head, 0)
    read(head)

    head = add_last(head, 7)
    read(head)

    head = remove_first(head)
    read(head)

    head = remove_last(head)
    read(head)



