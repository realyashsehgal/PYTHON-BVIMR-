#Write a python code to create and use a custom iterator.
# creating a custom iterator
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

# using the custom iterator
for number in CountUpto(5):
    print(number)
