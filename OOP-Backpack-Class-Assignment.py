print(" ")
class Backpack:
    def __init__(backpack, color, size):
        backpack.color = color
        backpack.size = size
        backpack.items = []
        backpack.open = False
        print(f"Backpack Created: Color:{backpack.color} Size: {backpack.size}\n")

    def putin(backpack,item):
        if backpack.open == True:
            backpack.items.append(item)
            print(f"{item} Added to backpack")
        else:
            print(f"Backpack is Closed. Can not add {item}")

    def take_out(backpack,item):
        try:    
            if backpack.open == True:
                backpack.items.remove(item)
                print(f"{item} removed from backpack")
            else:
                print(f"Backpack is Closed. Can not remove {item}")
        except ValueError:
            print(f"'{item}' not found in backpack")
    def backpackState(backpack, state):
        open_close = lambda state : True if state == "OPEN" else (False if state == "CLOSE" else "error")
        backpack.open = open_close(state)
        print(f"backpack is now {state}")

backpack1 = Backpack("blue","small")
backpack2 = Backpack("red","medium")
backpack3 = Backpack("green","large")

backpack1.backpackState("OPEN")
backpack1.putin("lunch")
backpack1.putin("jacket")
backpack1.backpackState("CLOSE")
backpack1.backpackState("OPEN")
backpack1.take_out("jacket")
backpack1.backpackState("CLOSE")
backpack1.take_out("lunch")
