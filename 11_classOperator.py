'''Write a class vector representing a vector of n dimensions.Overload the + and * operator which calculates 
the sum and the dot(.) product of them.Porgram saves as 11_classOperator.py '''
# 11_classOperator.py

class Vector:
    def __init__(self, components):
        """
        components: list or tuple of numbers representing vector components
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
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product

    def __str__(self):
        return f"Vector({self.components})"


# Testing
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)
print("v1 . v2 =", v1 * v2)
