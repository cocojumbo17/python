from avl_tree import *

class InvertedIndex:
    def __init__(self, avl_tree):
        self.avl_tree = avl_tree

    def index_document(self, document, document_id):
        lst = document.split()
        for word in lst:
            value = self.avl_tree.find(word)
            if value is None:
                s = TreeSet()
                s.add(document_id)
                self.avl_tree.insert(word, s)
            else:
                value.val.add(document_id)

    def search(self, word):
        return self.avl_tree.find(word)

    def get_average_documents_per_key(self):
        num_words = len(self.avl_tree)
        if num_words == 0:
            return 0
        else:
            num_docs = 0
            for word_docs_pair in self.avl_tree.get_keys():
                s = self.avl_tree.find(word_docs_pair)
                num_docs += len(s.val)
            res = num_docs / num_words
            num = round(res)
            return num

    def get_keys(self):
        self.avl_tree.printKeys()

def main():
    ii = InvertedIndex(AVLTree())

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
        node = ii.search(queries_item)
        if node is None:
            print(-1)
        else:
            s = node.val
            print(s)



    print(ii.get_average_documents_per_key())
    try:
        print_keys_flag = input()
        should_print_keys = print_keys_flag == 'print_keys'
    except:
        should_print_keys = False

    if should_print_keys:
        ii.get_keys()

if __name__ == '__main__': main()