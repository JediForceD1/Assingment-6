import CarDefinition # <- change this line to point to your class definition file

def main():
    # Create an instance of Car
    my_car = CarDefinition.Car("2008", "Honda Accord")

    print("my_car after instantiating:\n", my_car)

    my_car.setSpeed(2)
    print("my_car after my_car.setSpeed(2):\n", my_car)
    # Accelerate 5 times
    print ("car is accelerating: ")
    for i in range(5):
       my_car.accelerate()
       print ("Current speed: ", my_car.getSpeed())
    print()
    # Brake 7 times
    print ("car is braking: ")
    for i in range(7):
        my_car.brake()
        print ("Current speed: ", my_car.getSpeed())

    print("my_car values at program end:\n", my_car)


main()