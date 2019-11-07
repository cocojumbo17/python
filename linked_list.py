import math
import os
import random
import re
import sys


class Node:
    def __init__(self, value, next=None, prev=None):
        self._value = float(value)
        self._prev = prev
        self._next = next

    def GetPrev(self):
        return self._prev
    def GetNext(self):
        return self._next
    def GetValue(self):
        return self._value
    def SetPrev(self, prev):
        self._prev = prev
    def SetNext(self, next):
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push(self, value):
        N = Node(value)
        if self._size == 0:
            self._head = N
            self._tail = N
        else:
            N.SetPrev(self._tail)
            self._tail.SetNext(N)
            self._tail = N
        self._size += 1

    def pop(self):
        if self._size == 0:
            return None
        else:
            value = self._tail.GetValue()
            beforeTail = self._tail.GetPrev()
            if beforeTail is None:
                self._head = None
                self._tail = None
            else:
                beforeTail.SetNext(None)
                self._tail.SetPrev(None)
                self._tail = beforeTail
            self._size -= 1
            return value


    def unshift(self, value):
        N = Node(value)
        if self._size == 0:
            self._head = N
            self._tail = N
        else:
            N.SetNext(self._head)
            self._head.SetPrev(N)
            self._head = N
        self._size += 1


    def shift(self):
        if self._size == 0:
            return None
        else:
            value = self._head.GetValue()
            afterHead = self._head.GetNext()
            if afterHead is None:
                self._head = None
                self._tail = None
            else:
                afterHead.SetPrev(None)
                self._head.SetNext(None)
                self._head = afterHead
            self._size -= 1
            return value


    def insert(self, index, value):
        next_node = self.get(index)
        if next_node is None:
            self.push(value)
        else:
            prev_node = next_node.GetPrev()
            if prev_node is None:
                self.unshift(value)
            else:
                N = Node(value)
                N.SetNext(next_node)
                N.SetPrev(prev_node)
                next_node.SetPrev(N)
                prev_node.SetNext(N)
                self._size += 1




    def find(self, v):
        result = None
        curr_node = self._head
        while curr_node is not None:
            if curr_node.GetValue() == v:
                result = curr_node
                break
            else:
                curr_node = curr_node.GetNext()
        return result


    def get(self, index):
        i = 0
        result = None
        curr_node = self._head
        while curr_node is not None:
            if i == index:
                result = curr_node
                break
            else:
                curr_node = curr_node.GetNext()
                i += 1
        return result


    def size(self):
        return self._size

    def print(self):
        curr_node = self._head
        while curr_node is not None:
            print(curr_node.GetValue(), end=" ")
            curr_node = curr_node.GetNext()
        print()

    def print_r(self):
        curr_node = self._tail
        while curr_node is not None:
            print(curr_node.GetValue(), end=" ")
            curr_node = curr_node.GetPrev()
        print()


def main():
   
