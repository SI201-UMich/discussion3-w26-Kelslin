import math

class Rectangle():
    # Create the constructor "__init__" method

    # YOUR CODE HERE
    def __init__(self, width, length):
        self.width = width
        self.length = length



    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"Width: {self.width}, Length: {self.length}"


    # Create the "area_calculator" method

    # YOUR CODE HERE
    def area_calculator(self):
        return self.width*self.length 

    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE
    def __eq__(self, other):
        return self.area_calculator() == other.area_calculator() and self.width == other.width and self.length == other.length

    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())
    print()


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    r3 = Rectangle(10, 10)
    print(r3)
    print("Area:", r3.area_calculator())
    # call the __eq__ method
    print(r1 == r3)
    print()

    r4 = Rectangle(5, 30)
    print(r4)
    print("Area:", r4.area_calculator())
    # call the __eq__ method
    print(r2 == r4)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves

if __name__ == "__main__":
    main()