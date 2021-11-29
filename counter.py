class Counter:
    def __init__(self, value):
        self.value = value
        self.step = 1

    def increment(self):
        self.value += self.step

    def decrement(self):
        self.value -= self.step

    def set_value(self, new_value):
        self.value = new_value

    def set_step(self, new_step):
        self.step = new_step

    def get_value(self):
        return print(self.value)


myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
myCounter.get_value()
myCounter.set_step(5)
myCounter.decrement()
myCounter.get_value()
myCounter.set_value(100)
myCounter.increment()
myCounter.get_value()


class ScoreCounter(Counter):
    def __init__(self, value, name, age):
        super().__init__(value)
        self.name = name
        self.age = age
        self.winner = False

    def increment(self):
        self.value += self.step
        if self.value >= 12:
            self.winner = True


myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.winner)