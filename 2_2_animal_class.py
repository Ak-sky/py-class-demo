class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color