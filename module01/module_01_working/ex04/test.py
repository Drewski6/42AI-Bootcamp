# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from vector import Vector

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v3 = Vector([[1.0], [2.0], [3.0], [4.0]])
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
v4 = Vector([[1.0, 2.0, 3.0, 4.0]])

print("v1 = ", end='')
print(v1.values)
print("v2 = ", end='')
print(v2.values)
print("v3 = ", end='')
print(v3.values)
print("v4 = ", end='')
print(v4.values)

print("\ntesting dot products")
print("  v1\t", end='')
print(v1.values)
print("* v3\t", end='')
print(v3.values)
print("=\t", end='')
print(v1.dot(v3))
print()
print("  v2\t", end='')
print(v2.values)
print("* v4\t", end='')
print(v4.values)
print("=\t", end='')
print(v2.dot(v4))

print("\ntesting transpose")
print("v1")
print("Before")
print(v1.values)
print(v1.shape)
v1.T()
print("After")
print(v1.values)
print(v1.shape)

print("\ntesting transpose other direction")
print("v2")
print("Before")
print(v2.values)
print(v2.shape)
v2.T()
print("After")
print(v2.values)
print(v2.shape)

print("\ntesting initialization with int, and tuples")
v5 = Vector(5)
print("int init with '5'")
print(v5.values)
print(v5.shape)
v7 = Vector((1, 5))
print("tuple init with '(1, 5)'")
print(v7.values)
print(v7.shape)
v8 = Vector((10, 16))
print("tuple init with '(10, 16)'")
print(v8.values)
print(v8.shape)

print("\ntesting vector addition")
print("  v2\t", end='')
print(v2.values)
print("+ v3\t", end='')
print(v3.values)
print("=\t", end='')
print(v2 + v3)
print()
print("  v1\t", end='')
print(v1.values)
print("+ v4\t", end='')
print(v4.values)
print("=\t", end='')
print(v1 + v4)

print("\ntesting vector subtraction")
print("  v2\t", end='')
print(v2.values)
print("- v3\t", end='')
print(v3.values)
print("=\t", end='')
print(v2 - v3)
print()
print("  v1\t", end='')
print(v1.values)
print("- v4\t", end='')
print(v4.values)
print("=\t", end='')
print(v1 - v4)

print("\ntesting scalar division")
print("  v2\t", end='')
print(v2.values)
print("/\t5")
print("=\t", end='')
print(v2 / 5)
print()
print("  v1\t", end='')
print(v1.values)
print("/\t10")
print("=\t", end='')
print(v1 / 10)

print("\ntesting scalar multiplication")
print("  v2\t", end='')
print(v2.values)
print("*\t5")
print("=\t", end='')
print(v2 * 5)
print()
print("  v1\t", end='')
print(v1.values)
print("*\t10")
print("=\t", end='')
print(v1 * 10)

print("\ntesting __str__ printing")
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)

print("\ntesting __repr__ printing")
print(repr(v1))
print(repr(v2))
print(repr(v3))
print(repr(v4))
print(repr(v5))
