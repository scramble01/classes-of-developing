import threading
from threading import Thread

class Randomizes:
    def __init__(self, random_number, random_N_numbers):
        self.random_number = random_number
        self.random_N_numbers = random_N_numbers


    def random(self):    
        
        if self.random_number == 'random number':
            import random 
            a=random.randint(0,422)
            print(a)

        if self.random_N_numbers == 'random N numbers':
            import random
            a = 3
            for _ in range(a):               
                x = random.randint(0,422)
                print(x)

    def runcall(self):
        if __name__ == '__randoms all__':
            Thread(target = self.random_number).start()
            Thread(target = self.random_N_numbers).start()

run = Randomizes()
run.runcall()




