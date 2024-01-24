import random


class Primes:
    def __init__(self, num):
        self.num = num
        self.i = 1
        self.prime_num = []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        while self.i <= self.num:
            self.i += 1
            for prime in self.prime_num:
                if self.i % prime == 0:
                    break
            else:
                self.prime_num.append(self.i)
                return self.i
        raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')