def calculation_rectangle_area(length, width):
    return length*width
if __name__ == "__main__":
    length=float(input("Enter the length of the rectangle: "))
    width=float(input("Enter the with of the rectangle: "))

    area=calculation_rectangle_area(length,width)

    print(f"The area of the rectangle is: {area}")