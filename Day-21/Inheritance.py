class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breath(self):
        print("Inhale ")
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breath()
        print("Doing Under water")
    def swim(self):
        print("Swim ")
        
nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breath()