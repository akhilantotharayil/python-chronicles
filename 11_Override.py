'''Write a class vector representing a vector of n dimensions.Overload the + and * operator which calculates 
the sum and the dot(.) product of them.Overide the  __len() method on vector of this problem to display the dimension of this vector
Program saves as 11_Override.py '''

# 11_Override.py

class Vector:
    def __init__(self, components):
        """
        components: list or tuple representing vector components
        """
        self.components = list(components)
        self.n = len(components)

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have the same dimension for addition")
        summed = [a + b for a, b in zip(self.components, other.components)]
        return Vector(summed)

    def __mul__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have the same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __len__(self):
        return self.n

    def __str__(self):
        return f"Vector({self.components})"


# Testing
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)      # Vector addition
print("v1 . v2 =", v1 * v2)      # Dot product
print("Dimension of v1 =", len(v1))  # Dimension using __len__
