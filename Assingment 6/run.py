import CarDefinition

def main():
    self = CarDefinition.Car
    CarDefinition.Car.__init__(self, "2008", "Honda Accord")

    print(CarDefinition.Car.getMake(self))


main()