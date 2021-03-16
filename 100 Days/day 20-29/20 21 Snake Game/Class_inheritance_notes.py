
#this shows how to incorporate an existing class into a new class
#4-9 is the original class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# the first thing is after naming the class you put the previous class in ()
#then you type line 14-15 to import everything previously written. with super think "supercedes"
class Fish(Animal):
    def __init__(self):
        super().__init__()

    # 18-20 are how you modify something from the original class
    #for example now it will say "inhale, exhale. doing this under water"
    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()