class Television:
    def __init__(self, make, size, dop, isColor):
        self.__make = make
        self.__size = size
        self.__dop = dop
        self.__isColor = isColor
    
    def displayTelevision(self):
        print(f"Make: {self.__make}, Size: {self.__size}, Date of Purchase: {self.__dop}, Is Color: {self.__isColor}...")

# tv1 = Television("Sony", "32", "20-12-2020", True)
# tv1.displayTelevision()

# tv2 = Television("Philips", "55", "01-11-2022", True)
# tv2.displayTelevision()


class Room:
    def __init__(self, name, length, breadth, height, fans, lights, windows, doors):
        self.__name = name
        self.__length = length
        self.__breadth = breadth
        self.__height = height
        self.__fans = fans
        self.__lights = lights
        self.__windows = windows
        self.__doors = doors
        self.__wallarea = 2 * (length * breadth) * height * 0.80
        self.__floorarea = length * breadth
    
    def displayRoom(self):
        print(f"Name: {self.__name}, Fans: {self.__fans}, Lights: {self.__lights}, Windows: {self.__windows}, and Doors: {self.__doors}...")
        print(f"Floor Area: {self.__floorarea} and Wall Area: {self.__wallarea}...")
    
    def getFloorArea(self):
        return self.__floorarea
        
# room1 = Room("Living Room", 10, 12, 8, 2, 4, 3, 2)
# room1.displayRoom()
# print("Floor Area: ", room1.getFloorArea())

# room2 = Room("Study Room", 10, 20, 8, 4, 4, 5, 2)
# room2.displayRoom()
# print("Floor Area: ", room2.getFloorArea())

class House:
    def __init__(self, doorno, br, dr, hr, kr, dw, tv, doc):
        self.__doorno = doorno
        self.__bedRoom = br
        self.__diningRoom = dr
        self.__hallRoom = hr
        self.__kitchenRoom = kr
        self.__drawRoom = dw
        self.__television = tv
        self.__doc = doc
        self.__floorArea = br.getFloorArea() + dr.getFloorArea() + hr.getFloorArea() + kr.getFloorArea() + dw.getFloorArea()
        self.__plinthArea = self.__floorArea * 1.50
        self.__landArea = self.__floorArea * 1.75
    
    def displayHouse(self):
        print(f"Door No: {self.__doorno}, DOC: {self.__doc}, Plinth Area: {self.__plinthArea} and Land Area: {self.__landArea}...")
        self.__bedRoom.displayRoom()
        self.__diningRoom.displayRoom()
        self.__hallRoom.displayRoom()
        self.__kitchenRoom.displayRoom()
        self.__drawRoom.displayRoom()
        self.__television.displayTelevision()

# house1 = House("DN-1001",
#                Room("Bed Room", 10, 12, 8, 2, 4, 3, 2),
#                Room("Dining Room", 11, 14, 12, 4, 4, 3, 2),
#                Room("Hall Room", 10, 13, 8, 3, 4, 2, 2),
#                Room("Kitchen Room", 11, 11, 8, 2, 4, 2, 2),
#                Room("Drawing Room", 12, 12, 8, 6, 4, 3, 1),
#                Television("Sony", "32", "20-12-2020", True),
#                "20-12-2020"
#                )
# house1.displayHouse()


class Park:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
        self.__area = length * breadth
    
    def displayPark(self):
        print(f"Length: {self.__length}, Breadth: {self.__breadth} and Area of Park: {self.__area}")

# park1 = Park(10, 20)
# park1.displayPark()

# park2 = Park(30, 20)
# park2.displayPark()


class Block:
    def __init__(self, length, breadth, hh1, hh2, hh3, hh4, pk1):
        self.__house1 = hh1
        self.__house2 = hh2
        self.__house3 = hh3
        self.__house4 = hh4
        self.__park = pk1
        self.__area = length * breadth

    def displayBlock(self):
        print("Displaying the block details...")
        print("____________________House 1 details____________________")
        self.__house1.displayHouse()
        print("____________________House 2 details____________________")
        self.__house2.displayHouse()
        print("____________________House 3 details____________________")
        self.__house3.displayHouse()
        print("____________________House 4 details____________________")
        self.__house4.displayHouse()
        print("____________________Park details____________________")
        self.__park.displayPark()
        print("Area of the block is", self.__area)

block1 = Block(1045, 2000, 
                House("DN-1001",
                    Room("Bed Room", 8, 10, 7, 1, 3, 2, 1),
                    Room("Dining Room", 9, 12, 10, 3, 3, 2, 1),
                    Room("Hall Room", 7, 11, 7, 2, 3, 1, 1),
                    Room("Kitchen Room", 8, 10, 7, 1, 3, 1, 1),
                    Room("Drawing Room", 10, 11, 8, 4, 3, 2, 1),
                    Television("Samsung", "40", "15-01-2021", False),
                    "15-01-2021"
                    ),
                House("DN-1002",
                    Room("Bed Room", 12, 14, 9, 2, 4, 3, 2),
                    Room("Dining Room", 13, 16, 12, 4, 4, 3, 2),
                    Room("Hall Room", 11, 15, 9, 3, 4, 2, 2),
                    Room("Kitchen Room", 12, 14, 9, 2, 4, 2, 2),
                    Room("Drawing Room", 14, 14, 10, 6, 4, 3, 1),
                    Television("LG", "50", "20-02-2021", True),
                    "20-02-2021"
                    ),
                House("DN-1003",
                    Room("Bed Room", 10, 12, 8, 2, 4, 3, 2),
                    Room("Dining Room", 11, 14, 12, 4, 4, 3, 2),
                    Room("Hall Room", 10, 13, 8, 3, 4, 2, 2),
                    Room("Kitchen Room", 11, 11, 8, 2, 4, 2, 2),
                    Room("Drawing Room", 12, 12, 8, 6, 4, 3, 1),
                    Television("Sony", "32", "20-12-2020", True),
                    "20-12-2020"
                    ),
                House("DN-1004",
                    Room("Bed Room", 9, 11, 7, 1, 3, 2, 1),
                    Room("Dining Room", 10, 13, 10, 3, 3, 2, 1),
                    Room("Hall Room", 8, 12, 7, 2, 3, 1, 1),
                    Room("Kitchen Room", 9, 11, 7, 1, 3, 1, 1),
                    Room("Drawing Room", 11, 12, 8, 4, 3, 2, 1),
                    Television("Vizio", "55", "10-03-2021", False),
                    "10-03-2021"
                    ),
                Park(15, 25)
            )

block1.displayBlock()