
class House:
    def __init__(self, distance, cost, name):
        self.__distance = distance
        self.__monthly_Cost = cost
        self.__name = name

    def get_Distance(self):
        return self.__distance

    def get_Monthly_Cost(self):
        return self.__monthly_Cost

    def get_Name(self):
        return self.__name

    def set_Distance(self):
        return self.__distance

    def set_Monthly_Cost(self, cost):
        self.__monthly_Cost = cost

    def set_Name(self, name):
        self.__name = name


class Car:
    def __init__(self, mpg, price):
        self.__car_Mpg = mpg
        self.__gas_Price = price

    def get_Mpg(self):
        return self.__car_Mpg

    def get_Gas_Price(self):
        return self.__gas_Price

    def set_Mpg(self, mpg):
        self.__car_Mpg = mpg

    def set_Gas_Price(self, price):
        self.__gas_Price = price


houses = []
cars = []


def questions():
    print("Hello! What is your house's name?")
    name_Of_House = input(">")

    print("What is the monthly rent for your house?")
    house_Monthly_Cost = int(input('>'))

    print("How far is your house to the location? ")
    distance = float(input('>'))
    distance = distance*2

    print("What is the mpg of your car?")
    mpg = float(input('>'))

    print("What is the gas price?")
    gas_Price = float(input(">"))

    print("How many trips per week are you planning on doing?")
    amount_Of_Trips = int(input('>'))

    house = House(distance, house_Monthly_Cost, name_Of_House)
    car = Car(mpg, gas_Price)

    cars.append(car)
    houses.append(house)

    calculations(amount_Of_Trips)


def differences():
    house_1 = houses[0]
    house_2 = houses[1]
    car = cars[0]
    pass


def calculations(amount_Of_Trips):
    house = houses[0]
    car = cars[0]

    distance = float(house.get_Distance() * amount_Of_Trips)
    print("Every week you drive", distance, " miles. ")

    gallons = float(distance/car.get_Mpg())
    print("Every week, you use", gallons, "gallons of gas. ")

    cost = float(car.get_Gas_Price()*gallons)
    print("You spend $", cost, " a week on gas. ")

    cost = cost*4
    print("Monthly: $", cost)

    cost = cost*12
    print("Yearly: $", cost)


def main():
    questions()


if __name__ == '__main__':
    main()
