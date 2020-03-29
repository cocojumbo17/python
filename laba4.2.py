#!/bin/python3

import os
import sys
class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.build_min_heap()

    @staticmethod
    def parent(i):
        return (i-1) // 2

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

    def delete_min(self, is_sift=True):
        if self.size() == 0:
            return None
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        head = self.arr.pop()
        if is_sift:
            if self.size() > 0:
                self.sift_down(0)
        else:
            if self.size() > 0:
                first = self.arr.pop(0)
                self.arr.append(first)
                self.sift_up(self.size() - 1)
                self.sift_down(0)
        return head


#
# Complete the cookies function below.
#
def cookies(k, A):
    heap = Heap(A)
    operations = 0

    if len(A) == 0:
        print(operations)
    else:
        while(A[0] < k):
            if len(A) <= 1:
                break
            operations += 1
            least_sweet_cookie_1 = heap.delete_min(False)
            least_sweet_cookie_2 = heap.delete_min(False)
            sweetness = least_sweet_cookie_1 + 2 * least_sweet_cookie_2
            heap.insert(sweetness)
    if A[0] < k:
        print(-1)
    else:
        print(operations)

if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)



