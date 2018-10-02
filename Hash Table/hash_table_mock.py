class HashTable:
    def __init__(self, data=LinkedList()):
        self.data = data

    def put(self, key, value):
        hashcode = get_hash_code(key)
        index = convert_to_index(hashcode)
        list = data[index] # Linked List
        list.insert(key, value)
