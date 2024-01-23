import random


class СountIterator:
    count = 0

    def __iter__(self):
        return self

    def __next__(self):
        СountIterator.count += 1
        return СountIterator.count


my_iter = СountIterator()

for i_elem in my_iter:

    print(i_elem)
