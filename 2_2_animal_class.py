
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def description(self):
        print("======= Description of the Animal(Cat) =======")
        return f"Name: {self.name}\nAge: {self.age}\nColor: {self.color}\n"

    def speak(self, sound):
        print(super().speak(sound))
        return f"{self.name} meow: {sound}"

    def get_speed(self, speed):
        return f"The speed of the cats are generally {speed} km/h"


