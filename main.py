def add(num1: int, num2: int):  # define addation function
    return num2 + num1


def sub(num1: int, num2: int):  # define substraction function
    return num1 - num2


def mul(num1: int, num2: int):  # define multplation function
    return num2 * num1


def div(num1: int, num2: int):  # define divison function
    return num2 / num1


def triangle_area(base: float, high: float):  # define triangle area  function
    area = 0.5 * base * high
    return area


def circle_area(radus: float):  # define circle area  function
    area = 3.14 * radus * radus
    return area


def rectangle_area(length: float, highth: float):  # define rectangle area  function
    area = length * highth
    return area


while True:  # loop to print  my list
    selection = int(input(" 1.sum\n"
                          " 2.subtract\n"
                          " 3.Multiply\n"
                          " 4.Division\n "
                          " 5.calculate triangle area:\n"
                          " 6. calculate circle area\n"
                          " 7.calculate rectangle area\n"
                          " 8.exit "))

    if selection == 1:  # if user click 1 go to sum function
        num1 = int(input("first no:"))
        num2 = int(input("second no:"))
        print(f" sum of{num1}+{num2} is: ")
        print(add(num1, num2))

    elif selection == 2:  # if user click 2 go to sub function
        num1 = int(input("first no:"))
        num2 = int(input("second no:"))
        print(f" substract of{num1}-{num2} is: ")
        print(sub(num1, num2))

    elif selection == 3:  # if user click 3 go to mul function
        num1 = int(input("first no:"))
        num2 = int(input("second no:"))
        print(f" multiply of{num1}*{num2} is: ")
        print(mul(num1, num2))

    elif selection == 4:  # if user click 4 go to div function
        num1 = int(input("first no:"))
        num2 = int(input("second no:"))
        print(f" division of{num1}/{num2} is: ")
        print(div(num1, num2))

    elif selection == 5:  # if user click 5 go to triangle_area function
        base = int(input(" input base of area :"))
        high = int(input(" input base of area :"))
        print(f" triangle area with base ={base} and  high = {high} is: ")
        print(triangle_area(base, high))

    elif selection == 6:  # if user click 6 go to circle_area function
        radius = int(input(" input radius of circle :"))
        print(f" circle area with radius ={radius} is: ")
        print(circle_area(radius))

    elif selection == 7:  # if user click 7 go to rectangle_area function
        length = int(input(" input base of area :"))
        highth = int(input(" input base of area :"))
        print(f" triangle leng with high ={length} and  high = {highth} is: ")
        print(rectangle_area(length, highth))


    elif selection == 8:   # to exit
        exit()

    else:              # valid number
        print("valid choice enter correct in list :")
