class Car:
    wheels = 4
    doors = 4

    def __init__(self, brand, model, year, mileage, fuel=20, mpg=50, color="black"):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
        self.running = False
        self.fuel = fuel
        self.mpg = mpg

    def start(self):
        if self.running:
            print("Car is already running!")
        else:
            self.running = True
            print("Started the car.")

    def drive(self):
        if self.running:
            miles = int(input("How many miles do you want to drive? "))
            if miles > self.fuel * self.mpg:
                print("Sorry, not enough fuel!")
            else:
                self.fuel -= miles / self.mpg
                print(f"You drove {miles} miles, and used {miles / self.mpg} gallons of fuel.")
        else:
            print("You need to start the car first!")

    def refill(self):
        fuel = int(input("How much fuel do you want to refill? "))
        self.fuel += fuel
        print(f"You've refilled. Currently you have {self.fuel} gallons")

    def stop(self):
        self.running = False
        print("You've stopped the car.")


def main():
    toyota = Car("Toyota", "Corolla", 2002, 190000, color="green")
    toyota.start()
    toyota.drive()
    toyota.refill()
    toyota.stop()


if __name__ == "__main__":
    main()
