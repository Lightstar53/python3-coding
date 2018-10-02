class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def search_list(linked_list, key):
    while linked_list and linked_list.data != key:
        linked_list = linked_list.next_node
    return linked_list  # If no key found, None


def insert_node_after(node, new_node):
    new_node.next_node = node.next_node
    node.next_node = new_node


def delete_node_after(node):
    node.next_node = node.next_node.next_node


node1 = ListNode(12)
node2 = ListNode(14)

insert_node_after(node1, node2)
delete_node_after(node1)

print node2.data    # 14

print search_list(node1, 14)    # return ListNode

