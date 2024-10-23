# import numpy as np
#
# # Sample strokes for lines and shapes
# line_strokes = [
#     np.array([[0, 0], [1, 1]]),  # Diagonal line
#     np.array([[0, 0], [1, 0]]),  # Horizontal line
#     np.array([[0, 0], [0, 1]]),  # Vertical line
# ]
#
# circle_strokes = [
#     np.array([[0, 1], [0.707, 0.707], [1, 0], [0.707, -0.707], [0, -1], [-0.707, -0.707], [-1, 0], [-0.707, 0.707], [0, 1]]),  # Circle approximation
# ]
#
# square_strokes = [
#     np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]),  # Square
# ]
#
# triangle_strokes = [
#     np.array([[0, 0], [1, 1], [2, 0], [0, 0]]),  # Triangle
# ]
#
# # Combine all strokes into a single object array
# all_strokes = np.empty(len(line_strokes) + len(circle_strokes) + len(square_strokes) + len(triangle_strokes), dtype=object)
# all_strokes[:len(line_strokes)] = line_strokes
# all_strokes[len(line_strokes):len(line_strokes) + len(circle_strokes)] = circle_strokes
# all_strokes[len(line_strokes) + len(circle_strokes):] = square_strokes + triangle_strokes
#
# # Save to .npy file
# np.save('shapes_and_lines_dataset.npy', all_strokes)


# import numpy as np
#
# # Define your strokes including lines, shapes, and abstract forms
# shapes_and_lines = {
#     'line': [
#         np.array([[0, 0], [1, 1], [2, 2]]),  # Diagonal line
#         np.array([[0, 0], [2, 0]]),          # Horizontal line
#     ],
#     'circle': [
#         np.array([[0, 1], [1, 0], [0, -1], [-1, 0]]),  # Simple circle
#     ],
#     'square': [
#         np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]]),  # Square shape
#     ],
#     'triangle': [
#         np.array([[0, 1], [-1, -1], [1, -1]]),  # Triangle shape
#     ],
#     'abstract': [
#         np.array([[0, 0], [0.5, 1], [1, 0]]),  # Abstract shape 1
#         np.array([[0, 1], [0.5, 0], [1, 1], [0.5, 0.5]]),  # Abstract shape 2
#     ]
# }
#
# # Flatten the dataset for saving
# all_strokes = []
# for category, strokes in shapes_and_lines.items():
#     for stroke in strokes:
#         all_strokes.append(stroke)
#
# # Save the dataset
# np.save('shapes_lines_abstract_dataset.npy', all_strokes)


# import numpy as np
#
# # Define your strokes including lines, shapes, and abstract forms
# shapes_and_lines = {
#     'line': [
#         np.array([[0, 0], [1, 1], [2, 2]]),  # Diagonal line
#         np.array([[0, 0], [2, 0]]),          # Horizontal line
#     ],
#     'circle': [
#         np.array([[0, 1], [1, 0], [0, -1], [-1, 0]]),  # Simple circle
#     ],
#     'square': [
#         np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]]),  # Square shape
#     ],
#     'triangle': [
#         np.array([[0, 1], [-1, -1], [1, -1]]),  # Triangle shape
#     ],
#     'abstract': [
#         np.array([[0, 0], [0.5, 1], [1, 0]]),  # Abstract shape 1
#         np.array([[0, 1], [0.5, 0], [1, 1], [0.5, 0.5]]),  # Abstract shape 2
#     ]
# }
#
# # Flatten the dataset for saving
# all_strokes = []
# for category, strokes in shapes_and_lines.items():
#     for stroke in strokes:
#         all_strokes.append(stroke)
#
# # Convert to a NumPy array of type object
# all_strokes_array = np.array(all_strokes, dtype=object)
#
# # Save the dataset
# np.save('shapes_lines_abstract_dataset.npy', all_strokes_array)


import numpy as np
import random

def generate_circle(radius, num_points=50):
    """Generate points for a circle."""
    return np.array([[radius * np.cos(2 * np.pi * i / num_points),
                      radius * np.sin(2 * np.pi * i / num_points)] for i in range(num_points)])

def generate_square(size, num_points=50):
    """Generate points for a square."""
    points = []
    for i in range(num_points):
        t = (i / num_points) * 4
        if t < 1:
            points.append([-size / 2, -size / 2 + t * size])
        elif t < 2:
            points.append([-size / 2 + (t - 1) * size, size / 2])
        elif t < 3:
            points.append([size / 2, size / 2 - (t - 2) * size])
        else:
            points.append([size / 2 - (t - 3) * size, -size / 2])
    return np.array(points)

def generate_triangle(size, num_points=50):
    """Generate points for an equilateral triangle."""
    return np.array([[0, size],
                     [-size * np.sqrt(3) / 2, -size / 2],
                     [size * np.sqrt(3) / 2, -size / 2]])

def generate_random_stroke(num_points=10, spread=10):
    """Generate a random stroke (abstract shape)."""
    return np.random.rand(num_points, 2) * spread

# Create an empty list to hold all the strokes
all_strokes = []

# Generate and add shapes
all_strokes.append(generate_circle(radius=5))  # Circle
all_strokes.append(generate_square(size=10))    # Square
all_strokes.append(generate_triangle(size=10))   # Triangle

# Generate and add abstract strokes
for _ in range(100):  # Adjust number of abstract strokes as needed
    all_strokes.append(generate_random_stroke(num_points=random.randint(5, 20), spread=random.randint(5, 15)))

# Convert to a NumPy object array to handle varying shapes
all_strokes_array = np.array(all_strokes, dtype=object)

# Save the dataset to a .npy file
np.save('shapes_lines_abstract_dataset.npy', all_strokes_array, allow_pickle=True)

print("Dataset created and saved successfully.")
