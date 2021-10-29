
# # greeting function return type str, and the argument is expected to be of type str
# def greeting(name: str) -> str:

#     return 'Hello ' + name


# print(greeting('alex'))

Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:

    return [scalar*i for i in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])

print(new_vector)