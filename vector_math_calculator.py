import math

def vector_addition(v1, v2):
    """Perform vector addition."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_subtraction(v1, v2):
    """Perform vector subtraction."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    return [v1[i] - v2[i] for i in range(len(v1))]

def scalar_multiplication(v, scalar):
    """Perform scalar multiplication of a vector."""
    return [scalar * v[i] for i in range(len(v))]

def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    return sum(v1[i] * v2[i] for i in range(len(v1)))

def cross_product(v1, v2):
    """Calculate the cross product of two 3-dimensional vectors."""
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is defined only for 3-dimensional vectors.")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

def vector_projection(v1, v2):
    """Calculate the projection of vector v1 onto vector v2."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    dot_v1v2 = dot_product(v1, v2)
    mag_v2_squared = dot_product(v2, v2)
    return scalar_multiplication(v2, dot_v1v2 / mag_v2_squared)

def vector_reflection(v, normal):
    """Reflect vector v about the normal vector."""
    if len(v) != len(normal):
        raise ValueError("Vectors must have the same dimensions.")
    scalar = 2 * dot_product(v, normal) / dot_product(normal, normal)
    return vector_subtraction(v, scalar_multiplication(normal, scalar))

def vector_refraction(v, normal, eta):
    """Refract vector v through the surface with normal vector normal and index of refraction eta."""
    if len(v) != len(normal):
        raise ValueError("Vectors must have the same dimensions.")
    dot_vn = dot_product(v, normal)
    k = 1.0 - eta * eta * (1.0 - dot_vn * dot_vn)
    if k < 0:
        return [0] * len(v)  # Total internal reflection
    else:
        return vector_subtraction(scalar_multiplication(v, eta), scalar_multiplication(normal, eta * dot_vn + math.sqrt(k)))

def vector_face_forward(n, i, ng):
    """Face forward operation for vectors."""
    dot_ni = dot_product(n, i)
    return i if dot_ni < 0 else scalar_multiplication(i, -1)

def vector_scale(v, s):
    """Scale (multiply) vector v by scalar s."""
    return [v[i] * s for i in range(len(v))]

def vector_distance(v1, v2):
    """Calculate the Euclidean distance between vectors v1 and v2."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    return math.sqrt(sum((v1[i] - v2[i]) ** 2 for i in range(len(v1))))

def vector_length(v):
    """Calculate the length (magnitude) of vector v."""
    return math.sqrt(sum(v[i] ** 2 for i in range(len(v))))

def vector_absolute(v):
    """Calculate the absolute value (magnitude) of vector v."""
    return [abs(v[i]) for i in range(len(v))]

def vector_minimum(v1, v2):
    """Calculate the component-wise minimum of vectors v1 and v2."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    return [min(v1[i], v2[i]) for i in range(len(v1))]

def vector_maximum(v1, v2):
    """Calculate the component-wise maximum of vectors v1 and v2."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions.")
    return [max(v1[i], v2[i]) for i in range(len(v1))]

def vector_floor(v):
    """Apply the floor function to each component of vector v."""
    return [math.floor(v[i]) for i in range(len(v))]

def vector_ceil(v):
    """Apply the ceiling function to each component of vector v."""
    return [math.ceil(v[i]) for i in range(len(v))]

def vector_snap(v, increment):
    """Snap each component of vector v to the nearest multiple of increment."""
    return [round(v[i] / increment) * increment for i in range(len(v))]

def vector_wrap(v, min_values, max_values):
    """Wrap each component of vector v between min_values and max_values."""
    if len(v) != len(min_values) or len(v) != len(max_values):
        raise ValueError("Vector dimensions must match min_values and max_values.")
    return [min(max(v[i], min_values[i]), max_values[i]) for i in range(len(v))]

def vector_sin(v):
    """Apply the sine function to each component of vector v."""
    return [math.sin(v[i]) for i in range(len(v))]

def vector_cos(v):
    """Apply the cosine function to each component of vector v."""
    return [math.cos(v[i]) for i in range(len(v))]

def vector_tan(v):
    """Apply the tangent function to each component of vector v."""
    return [math.tan(v[i]) for i in range(len(v))]

import math

# Define all vector operations here...

def print_vector(v):
    """Print the vector in a readable format."""
    print("[", end="")
    for i in range(len(v)):
        if i < len(v) - 1:
            print(f"{v[i]}, ", end="")
        else:
            print(f"{v[i]}", end="")
    print("]")

def main():
    print("Vector Math Calculator")
    while True:
        print("\nAvailable Operations:")
        print("1. Vector Addition")
        print("2. Vector Subtraction")
        print("3. Scalar Multiplication")
        print("4. Dot Product")
        print("5. Cross Product (for 3-dimensional vectors)")
        print("6. Vector Projection")
        print("7. Vector Reflection")
        print("8. Vector Refraction")
        print("9. Face Forward")
        print("10. Vector Scaling")
        print("11. Vector Distance")
        print("12. Vector Length (Magnitude)")
        print("13. Vector Absolute Value")
        print("14. Vector Minimum")
        print("15. Vector Maximum")
        print("16. Vector Floor")
        print("17. Vector Ceiling")
        print("18. Vector Snap")
        print("19. Vector Wrap")
        print("20. Vector Sine")
        print("21. Vector Cosine")
        print("22. Vector Tangent")
        print("0. Exit")
        print()

        try:
            choice = int(input("Enter operation choice (0-22): "))
            if choice == 0:
                print("Exiting...")
                break
            elif choice < 1 or choice > 22:
                raise ValueError("Invalid choice. Please enter a number between 0 and 22.")

            if choice in [1, 2]:
                v1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(",")))

                if choice == 1:
                    result = vector_addition(v1, v2)
                    print("Result of Vector Addition:")
                    print_vector(result)
                elif choice == 2:
                    result = vector_subtraction(v1, v2)
                    print("Result of Vector Subtraction:")
                    print_vector(result)

            elif choice == 3:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                scalar = float(input("Enter scalar value: "))
                result = scalar_multiplication(v, scalar)
                print("Result of Scalar Multiplication:")
                print_vector(result)

            elif choice == 4:
                v1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(",")))
                result = dot_product(v1, v2)
                print("Result of Dot Product:")
                print(result)

            elif choice == 5:
                v1 = list(map(float, input("Enter vector 1 (3-dimensional, comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (3-dimensional, comma-separated values): ").split(",")))
                result = cross_product(v1, v2)
                print("Result of Cross Product:")
                print_vector(result)

            elif choice == 6:
                v1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(",")))
                result = vector_projection(v1, v2)
                print("Result of Vector Projection:")
                print_vector(result)

            elif choice == 7:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                normal = list(map(float, input("Enter normal vector (comma-separated values): ").split(",")))
                result = vector_reflection(v, normal)
                print("Result of Vector Reflection:")
                print_vector(result)

            elif choice == 8:
                v = list(map(float, input("Enter incident vector (comma-separated values): ").split(",")))
                normal = list(map(float, input("Enter normal vector (comma-separated values): ").split(",")))
                eta = float(input("Enter index of refraction (eta): "))
                result = vector_refraction(v, normal, eta)
                print("Result of Vector Refraction:")
                print_vector(result)

            elif choice == 9:
                n = list(map(float, input("Enter normal vector (comma-separated values): ").split(",")))
                i = list(map(float, input("Enter incident vector (comma-separated values): ").split(",")))
                ng = list(map(float, input("Enter normalized normal vector (comma-separated values): ").split(",")))
                result = vector_face_forward(n, i, ng)
                print("Result of Face Forward Operation:")
                print_vector(result)

            elif choice == 10:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                s = float(input("Enter scaling factor: "))
                result = vector_scale(v, s)
                print("Result of Vector Scaling:")
                print_vector(result)

            elif choice == 11:
                v1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(",")))
                result = vector_distance(v1, v2)
                print("Distance between Vector 1 and Vector 2:")
                print(result)

            elif choice == 12:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_length(v)
                print("Length (Magnitude) of the Vector:")
                print(result)

            elif choice == 13:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_absolute(v)
                print("Absolute Value (Magnitude) of the Vector:")
                print_vector(result)

            elif choice == 14:
                v1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(",")))
                result = vector_minimum(v1, v2)
                print("Component-wise Minimum of Vector 1 and Vector 2:")
                print_vector(result)

            elif choice == 15:
                v1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(",")))
                v2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(",")))
                result = vector_maximum(v1, v2)
                print("Component-wise Maximum of Vector 1 and Vector 2:")
                print_vector(result)

            elif choice == 16:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_floor(v)
                print("Floor of each component of the Vector:")
                print_vector(result)

            elif choice == 17:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_ceil(v)
                print("Ceiling of each component of the Vector:")
                print_vector(result)

            elif choice == 18:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                increment = float(input("Enter increment value for snapping: "))
                result = vector_snap(v, increment)
                print(f"Vector Snapped to Nearest Multiple of {increment}:")
                print_vector(result)

            elif choice == 19:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                min_values = list(map(float, input("Enter min values (comma-separated values): ").split(",")))
                max_values = list(map(float, input("Enter max values (comma-separated values): ").split(",")))
                result = vector_wrap(v, min_values, max_values)
                print("Vector Wrapped between Min and Max Values:")
                print_vector(result)

            elif choice == 20:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_sin(v)
                print("Sine (sin) of each component of the Vector:")
                print_vector(result)

            elif choice == 21:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_cos(v)
                print("Cosine (cos) of each component of the Vector:")
                print_vector(result)

            elif choice == 22:
                v = list(map(float, input("Enter vector (comma-separated values): ").split(",")))
                result = vector_tan(v)
                print("Tangent (tan) of each component of the Vector:")
                print_vector(result)

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print(f"Error: {e}")

        # Ask user if they want to perform another operation
        try:
            continue_choice = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                break
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
