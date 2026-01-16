import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = ""
        for line in range(self.height):
            result += "*" * self.width + "\n"
        return result

    def get_amount_inside(self, inside_object):
        width_par = int(self.width / inside_object.width)
        height_par = int(self.height / inside_object.height)
        return width_par * height_par

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_width(self, new_length):
        self.width = new_length
        self.height = new_length

    def set_height(self, new_length):
        self.width = new_length
        self.height = new_length

    def set_side(self, new_length):
        self.width = new_length
        self.height = new_length

    def __str__(self):
        return f"Square(side={self.width})"


rect = Rectangle(3, 6)
print(rect.get_picture())
print(rect.get_diagonal())

gog = Square(5)
print(gog.get_diagonal())