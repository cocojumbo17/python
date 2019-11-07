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

def parseCommand(command):
    """
    parse command in string to binary format
    :param command: string
    :return: list of:
    elem0 - boolean flag (true - no error, false - error of format)
    elem1 - command (1 - push, 2 - pop, 3 - unshift, 4 - shift, 5 - insert)
    elem2 - optional param of functions (push - float element, unshift - float element, insert - int index)
    elem3 - optional param of functions (insert - float element)
    """
    parts = command.split()
    if len(parts) == 0:
        return [False]
    if parts[0] == 'push':
        if len(parts) != 2:
            return [False]
        el = float(parts[1])
        return [True, 1, el]
    if parts[0] == 'pop':
        return [True, 2]
    if parts[0] == 'unshift':
        if len(parts) != 2:
            return [False]
        el = float(parts[1])
        return [True, 3, el]
    if parts[0] == 'shift':
        return [True, 4]
    if parts[0] == 'insert':
        if len(parts) != 3:
            return [False]
        index = int(parts[1])
        el = float(parts[2])
        return [True, 5, index, el]
    return [False]


def executeCommand(command, ll):
    if command[1] == 1:
        ll.push(command[2])
    elif command[1] == 2:
        ll.pop()
    elif command[1] == 3:
        ll.unshift(command[2])
    elif command[1] == 4:
        ll.shift()
    elif command[1] == 5:
        ll.insert(command[2], command[3])

def main():
    N = int(input('Number of elements N='))
    str_elements = input('Elements are:')
    all_elements = str_elements.split()
    if len(all_elements) != N:
        print('Incorrect number of elements')
        return
    our_list = LinkedList()
    for el in all_elements:
        our_list.push(float(el))

    M = int(input('Number of commands M='))
    for i in range(M):
        str_command = input(f'Command #{i}:')
        bin_command = parseCommand(str_command)
        if bin_command[0]:
            executeCommand(bin_command, our_list)
        else:
            print("Wrong command's format")
            return
    our_list.print_r()
    our_list.print()


main()