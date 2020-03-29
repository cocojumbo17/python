def get_hash(key):
    hashsum = 0
    if isinstance(key, (list, str)):
        for character in key:
            hashsum = ord(character) + (hashsum << 5) - hashsum
    else:
        hashsum = key

    return hashsum


class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashTable:

    def __init__(self, initial_capacity=4, load_factor=0.75):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * initial_capacity
        self.load_factor = load_factor

    def __len__(self):
        return self.size

    def find_index(self, key):
        return get_hash(key) % self.capacity

    def insert(self, key, value):
        current_load_factor = (len(self) + 1) / self.capacity
        if current_load_factor > self.load_factor:
            self.resize(self.capacity * 2)

        index = self.find_index(key)

        node = self.buckets[index]
        while node is not None:
            if key == node.key:
                node.value = value
                return
            node = node.next

        self.buckets[index] = Node(key, value, self.buckets[index])
        self.size += 1

    def find(self, key):
        index = self.find_index(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def delete(self, key):
        index = self.find_index(key)
        node = self.buckets[index]
        previous_node = None
        while node is not None:
            if key == node.key:
                if previous_node:
                    previous_node.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return node.value
            previous_node = node
            node = node.next
        return None

    def resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                key = node.key
                index = self.find_index(key)
                HashTable.insert_at_index(new_arr, key, node.value, index)
                node = node.next
        self.buckets = new_arr
        self.capacity = new_capacity

    @staticmethod
    def insert_at_index(arr, key, value, index):
        node = arr[index]
        while node is not None:
            node = node.next
        arr[index] = Node(key, value, arr[index])

    def __str__(self):
        key_value_pairs = []
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                key_value_pairs.append((node.key, node.value))
                node = node.next
        return str(key_value_pairs)

    def __iter__(self):
        self.index_of_cur_bucket = 0
        self.cur_node = None
        return self

    def __next__(self):
        if self.index_of_cur_bucket == len(self.buckets) and self.cur_node is None:
            raise StopIteration
        else:
            while self.cur_node is None and self.index_of_cur_bucket < len(self.buckets):
                self.cur_node = self.buckets[self.index_of_cur_bucket]
                self.index_of_cur_bucket += 1
            if self.cur_node is not None:
                node = self.cur_node
                self.cur_node = self.cur_node.next
                return node
            else:
                raise StopIteration

    def get_keys(self):
        keys = []
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                keys.append(node.key)
                node = node.next
        return keys


class HashSet:
    def __init__(self):
        self.hash_table = HashTable()

    def add(self, val):
        self.hash_table.insert(val, val)

    def __contains__(self, item):
        return self.hash_table.find(item) is not None

    def __str__(self):
        keys = self.hash_table.get_keys()
        res = ''
        for k in keys:
            res += str(k) + ' '
        return res

    def __len__(self):
        return len(self.hash_table)


class InvertedIndex:
    def __init__(self, hash_table):
        self.hash_table = hash_table

    def index_document(self, document, document_id):
        lst = document.split()
        for word in lst:
            val = self.hash_table.find(word)
            if val is None:
                s = HashSet()
                s.add(document_id)
                self.hash_table.insert(word, s)
            else:
                val.add(document_id)

    def search(self, word):
        return self.hash_table.find(word)

    def get_average_documents_per_key(self):
        num_words = len(self.hash_table)
        num_docs = 0
        for word_docs_pair in self.hash_table:
            num_docs += len(word_docs_pair.value)
        res = num_docs / num_words
        num = int(res + (0.5 if res > 0 else -0.5))
        return num


def main():
    ii = InvertedIndex(HashTable(1000))

    num_documents = int(input().strip())

    documents = []

    for i in range(num_documents):
        documents_item = input()
        documents.append(documents_item)
        ii.index_document(documents_item, i)

    num_queries = int(input().strip())

    queries = []

    for _ in range(num_queries):
        queries_item = input()
        queries.append(queries_item)
        val = ii.search(queries_item)
        if val is None:
            print(-1)
        else:
            print(val)

    print(ii.get_average_documents_per_key())


if __name__ == '__main__': main()
