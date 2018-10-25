import CarDefinition

def main():
    # Create an instance of Car
    #my_car = CarDefinition.Car("2008", "Honda Accord")
    
    CarDefinition.Car.__init__('self', '2008', 'Honda Accord')

    #print(my_car)

main()