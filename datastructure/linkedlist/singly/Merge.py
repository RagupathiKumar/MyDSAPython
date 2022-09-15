from Node import Node, get_default
from Crud import read, add_values


def merge_sorted_ll(head_1, head_2):

    if head_1 is None:
        return head_2
    elif head_2 is None:
        return head_1

    curr_a = head_1
    curr_b = head_2
    head = None
    curr = None

    while curr_a is not None and curr_b is not None:

        if curr_a.value <= curr_b.value:
            value = curr_a.value
            curr_a = curr_a.next
        elif curr_b.value < curr_a.value:
            value = curr_b.value
            curr_b = curr_b.next
        # else:
        #     value = curr_a.value
        #     curr_a = curr_a.next
        #     curr_b = curr_b.next

        if head is None:
            head = Node(value)
            curr = head
        else:
            curr.next = Node(value)
            curr = curr.next

    while curr_a is not None:
        curr.next = Node(curr_a.value)
        curr = curr.next
        curr_a = curr_a.next

    while curr_b is not None:
        curr.next = Node(curr_b.value)
        curr = curr.next
        curr_b = curr_b.next

    return head


if __name__ == "__main__":
    head_a = get_default()
    add_values(head_a, 6, 7, 8, 9, 12)
    read(head_a)

    head_b = Node(4)
    add_values(head_b, 5, 6, 10, 11)
    read(head_b)

    head_final = merge_sorted_ll(head_a, head_b)
    read(head_final)
