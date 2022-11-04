from Node import get_default, Node


def read(head_node):
    curr = head_node
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print("")


def read_reverse(head_node):

    if head_node is None:
        return

    curr = head_node
    while curr.next is not None:
        curr = curr.next

    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.prev
    print("")


def add_first(head_node, value):
    node = Node(value)

    if head_node is not None:
        node.next = head_node
        head_node.prev = node

    return node


def add_last(head_node, value):
    node = Node(value)

    if head_node is None:
        return node

    last = head_node
    while last.next is not None:
        last = last.next

    last.next = node
    node.prev = last
    return head_node


def add_after(head_node, value, after_node_value):
    node = Node(value)

    current = head_node
    while current is not None and current.value != after_node_value:
        current = current.next

    if current is not None:

        temp = current.next
        if temp is not None:
            node.next = temp
            temp.prev = node

        current.next = node
        node.prev = current


def remove_first(head_node):

    if head_node is None or head_node.next is None:
        return None

    next_node = head_node.next
    next_node.prev = None
    return next_node


def remove_last(head_node):

    if head_node is None or head_node.next is None:
        return None

    last_node = head_node
    while last_node.next is not None:
        last_node = last_node.next

    last_node.prev.next = None
    last_node.prev = None
    return head_node


def remove(head_node, value):

    current = head_node
    while current is not None and current.value != value:
        current = current.next

    if current is not None:

        if current.prev is not None:
            current.prev.next = current.next
        else:
            head_node = current.next

        if current.next is not None:
            current.next.prev = current.prev

        current.prev = None
        current.next = None

    return head_node


if __name__ == "__main__":
    head = get_default()
    read(head)

    head = add_first(head, 5)
    read(head)

    head = add_last(head, 6)
    read(head)

    add_after(head, 7, 4)
    read(head)

    head = remove_first(head)
    read(head)

    head = remove_last(head)
    read(head)

    head = remove(head, 1)
    read(head)

    head = remove(head, 7)
    read(head)

    head = remove(head, 3)
    read(head)

    read_reverse(head)
