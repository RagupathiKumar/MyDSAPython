from Node import get_default, Node


def read(head_node):

    if head_node is None:
        return

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
        node.prev = node
    else:
        last = head_node.prev

        last.next = node
        node.prev = last

        head_node.prev = node
        node.next = head_node

    return node


def add_last(head_node, value):
    node = Node(value)

    if head_node is None:
        node.next = node
        node.prev = node
        head_node = node
    else:
        last = head_node.prev

        last.next = node
        node.prev = last

        head_node.prev = node
        node.next = head_node

    return head_node


def remove_first(head_node):

    if head_node is None or \
            head_node.next is head_node:
        return None

    prev_node = head_node.prev
    next_node = head_node.next

    prev_node.next = next_node
    next_node.prev = prev_node

    return next_node


def remove_last(head_node):

    if head_node is None or \
            head_node.next is head_node:
        return None

    last = head_node.prev
    prev_last = last.prev

    prev_last.next = head_node
    head_node.prev = prev_last

    return head_node


if __name__ == "__main__":
    head = get_default()
    read(head)

    head = add_first(head, 6)
    read(head)

    head = add_last(head, 7)
    read(head)

    head = remove_first(head)
    read(head)

    head = remove_last(head)
    read(head)

