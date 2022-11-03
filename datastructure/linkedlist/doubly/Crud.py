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


if __name__ == "__main__":
    head = get_default()

    head = add_first(head, 5)
    head = add_last(head, 6)
    add_after(head, 7, 4)
    read(head)
    read_reverse(head)
