import math

# Rectangle class
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Update width
    def set_width(self, width):
        self.width = width

    # Update height
    def set_height(self, height):
        self.height = height

    # Return area
    def get_area(self):
        return self.width * self.height

    # Return perimeter
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Return diagonal
    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    # Return visual representation
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        
        picture = ''
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    # Calculate how many times another shape fits inside
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    # String representation of Rectangle object
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Square class
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_width(self, side):
        # Square keeps both sides equal
        self.width = side
        self.height = side

    def set_height(self, side):
        # Square keeps both sides equal
        self.height = side
        self.width = side

    def set_side(self, side):
        # Set both width and height to same value
        self.width = side
        self.height = side

    # String representation of Square object
    def __str__(self):
        return f"Square(side={self.width})"