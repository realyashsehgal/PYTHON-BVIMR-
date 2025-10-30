class CountUpto:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration

for number in CountUpto(5):
    print(number)

from Signature_folder.Signature import sign
sign()