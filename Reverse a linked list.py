# Reverse a linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Original linked list:")
linked_list.display()

linked_list.head = reverse_linked_list(linked_list.head)
print("Reversed linked list:")
linked_list.display()