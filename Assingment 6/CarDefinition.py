class Car:

    
    
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    ############# year_model################
    def setYear_model(self, year_model):
        self.__year_model = year_model

    def getYear_model(self):
        return self.__year_model

    ############# Make################
    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    ############# speed################
    def setSpeed(self, inp_speed):
        if inp_speed < 0:
            print("Speed cannot be negative")
        else:
            self.__speed = inp_speed

    def getSpeed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            print("Your speed cannot be negitive.")
            self.__speed = 0


    ############# str ############
    def __str__(self):
        return "Make : " + self.__make + ", Model Year :" + \
            self.__year_model + ", speed =" + str(self.__speed)


