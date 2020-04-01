from hashtable import HashTable, HashSet

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
        if num_words == 0:
            return 0
        else:
            res = num_docs / num_words
            num = round(res)
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

    set_B = ii.search('В')
    print(f'size = {len(set_B)} set={set_B}')

    print(ii.get_average_documents_per_key())


if __name__ == '__main__': main()
