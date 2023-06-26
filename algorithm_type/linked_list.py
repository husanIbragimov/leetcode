"""
Linked List
"""


class Node:
    """ Node (tugun) object """

    def __init__(self, data):
        self.data = data
        self.next = Node


class LinkedList:
    """ Linked List object """

    def __init__(self):
        self.head = Node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """ Add new node data """
        # create new node
        new_node = Node(new_data)
        # list boshini keyingi o'ringa qo'yish
        new_node.next = self.head
        # yangi nodeni list boshiga qo'yamiz
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        """ Biror tugundan so'ng tugun qo'shish """

        if prev_node is Node:
            print("Not found node")
            return
        # yangi tugun qo'shamiz'
        new_node = Node(new_data)
        # yangi tugunni keyingi tugunga bog'laymiz'
        new_node.next = prev_node.next
        # avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node

    def append(self, new_data):
        """ List oxiriga tugun qo'shish """

        new_node = Node(new_data)
        # bo'shemasligiga tekshirish
        if self.head is Node:
            # Bo'sh bo'lsa yangi tugun list boshi
            self.head = new_node
            return
        # aks xolda list oxiriga boramiz
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        # Listni boshidan topib olamiz
        temp = self.head
        # birichi tugunni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp = Node
            return
            # aks xolda keyingi tugunni qarasin
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # agar qiymat topilmasa
        if temp == Node:
            return

        # Tugunli listdan ochiramiz
        prev.next = temp.next
        temp = Node
