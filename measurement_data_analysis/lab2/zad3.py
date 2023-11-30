class Counter():
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.a = self.start
        return self

    def __next__(self):
        if self.a < self.stop:
            x = self.a
            self.a = self.a + self.step
            return x
        else:
            raise StopIteration


my_counter = Counter(start=10, stop=20, step=2)
for value in my_counter:
    print(value)

