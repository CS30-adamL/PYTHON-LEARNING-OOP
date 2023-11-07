# Create a Car class
class Car:
    # Define constructor method with parameters
    def __init__(car, year, make, model):
        # Add properties to empty car object
        car.year = year
        car.make = make
        car.model = model
        car.running = False
        car.speed = 0
        print(f"Car created: {year} {make} {model}")

    # Methods (Functions / Behaviour)
    def Ignition(car, bool):
        on_off = lambda Ignition_state : True if Ignition_state == "ON" else (False if Ignition_state == "OFF" else "error")
        if on_off(bool) != "error":
            car.running = on_off(bool)
        else:
            bool = "ERROR"
        
        print(f"Car is now: {bool}")


    def changeSpeed(car, newSpeed):
        car.speed = newSpeed
        print(f"Car Speed is now: {car.speed}km/h")


car1 = Car(2018,"FORD","Mustang")
car2 = Car(1962,"Ferrari","250 GTO")
car3 = Car(2016,"Bugatti","Chiron")

car1.Ignition("ON")
car1.changeSpeed(50)
car1.changeSpeed(80)
car1.changeSpeed(0)
car1.Ignition("OFF")