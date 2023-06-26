from algorithm_type.linked_list import Node, LinkedList

llist = LinkedList()

# create 3 node
llist.head = Node('Monday')
tuesday = Node('Tuesday')
wednesday = Node('Wednesday')

# connecting node
llist.head.next = tuesday
tuesday.next = wednesday
print(llist.head.next.next.data, '\n')
# console ga chiqarish
# llist.print_list()

# List boshiga yangi node (tugun) qo'shish
llist.push('Sunday')
# llist.print_list()

llist.insert_after(llist.head.next.next, 'Tuesday night')
llist.print_list()

# List oxiriga tugun qo'shish
llist.append('Thursday')
llist.append('Friday')
# llist.print_list()

llist.delete_node('Sunday')
llist.delete_node('Monday')

llist.print_list()

