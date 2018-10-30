import CarDefinition

'''
Aaron McCormick
Assingment 6
10/30/2018
'''

def main():

    self = CarDefinition.Car
    CarDefinition.Car.__init__(self, "2017", "Chevy Cruze")

    print("This is my car ", self.getYear_model(self), " ", self.getMake(self), sep = "")

    self.setSpeed(self, 2)
    # Accelerate 5 times
    print ("car is accelerating: ")
    for i in range(5):
        self.accelerate(self)
        print ("Current speed: ", self.getSpeed(self))

    print()
    # Brake 7 times
    print ("car is braking: ")
    for i in range(7):
        self.brake(self)
        print ("Current speed: ", self.getSpeed(self))
main()