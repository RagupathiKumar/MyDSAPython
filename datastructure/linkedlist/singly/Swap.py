from Node import Node, get_default
from Crud import add_values, read


def swap(head_node, a, b):

    if a is None or b is None \
            or a == b or head_node is None:
        return head_node

    prev_a = node_a = prev_b = node_b = None

    prev = None
    curr = head_node
    while curr is not None:

        if curr.value == a:
            prev_a = prev
            node_a = curr
        elif curr.value == b:
            prev_b = prev
            node_b = curr

        if node_a is None or node_b is None:
            prev = curr
            curr = curr.next
        else:
            break

    # swap here
    if node_a is not None and node_b is not None:

        if prev_a is None:
            head_node = node_b
        else:
            prev_a.next = node_b

        if prev_b is None:
            head_node = node_a
        else:
            prev_b.next = node_a

        temp_node_b_next = node_b.next
        if node_a.next == node_b:
            node_b.next = node_a
        else:
            node_b.next = node_a.next

        if node_a == temp_node_b_next:
            node_a.next = node_b
        else:
            node_a.next = temp_node_b_next

    return head_node


if __name__ == '__main__':
    head = get_default()
    add_values(head, 4, 5, 6, 7, 8, 9, 10)
    read(head)

    # case normal
    head = swap(head, 3, 7)
    read(head)

    # case end
    head = swap(head, 1, 10)
    read(head)

    # case normal inverted input
    head = swap(head, 9, 2)
    read(head)

    # case end inverted input
    head = swap(head, 10, 1)
    read(head)

    # case next to each other
    head = swap(head, 4, 5)
    read(head)

    # case next to each other inverted input
    head = swap(head, 6, 4)
    read(head)

    # case extreme only 2 nodes
    head = Node(1)
    head.next = Node(2)
    head = swap(head, 1, 2)
    read(head)

