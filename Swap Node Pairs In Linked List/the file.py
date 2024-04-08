from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    new_head.next, head.next = head, swap_pairs(new_head.next)
    return new_head
