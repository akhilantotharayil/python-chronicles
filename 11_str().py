'''Write __str() method to print the vector as follows: 7i+ 8j +10k Assume vector of dimention 3 for this problem.Program saved as 11_str().py'''

# 11_str().py

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x  # i-component
        self.y = y  # j-component
        self.z = z  # k-component

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


# Testing
v = Vector3D(7, 8, 10)
print(v)
