class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.build_min_heap()

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return i * 2 + 1

    @staticmethod
    def right(i):
        return i * 2 + 2

    def size(self):
        return len(self.arr)

    def insert(self, e):
        self.arr.append(e)
        self.sift_up(self.size() - 1)

    def sift_up(self, i):
        while i > 0:
            parent = Heap.parent(i)
            if self.arr[i] < self.arr[parent]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent

    def min_child(self, i):
        left = Heap.left(i)
        right = Heap.right(i)
        length = self.size()
        smallest = i
        if left < length and self.arr[i] > self.arr[left]:
            smallest = left
        if right < length and self.arr[smallest] > self.arr[right]:
            smallest = right
        return smallest

    def sift_down(self, i):
        while True:
            min_child = self.min_child(i)
            if i == min_child:
                break
            self.arr[i], self.arr[min_child] = self.arr[min_child], self.arr[i]
            i = min_child

    def build_min_heap(self):
        for i in reversed(range(len(self.arr) // 2)):
            self.sift_down(i)

    def delete_min(self):
        if self.size() == 0:
            return None
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        head = self.arr.pop()
        if self.size() > 0:
            self.sift_down(0)
        return head


def heap_sort(arr):
    heap = Heap(arr)
    sorted_arr = []
    while heap.size() > 0:
        sorted_arr.append(heap.delete_min())
    return sorted_arr
