# import numpy as np
#
#
# def calculate_distance(user_stroke, original_stroke):
#     # Calculate the distance from user stroke to all points in the original stroke
#     distances = []
#     for point in original_stroke:
#         # Calculate distance from each point in the original stroke to the user stroke
#         min_distance = np.min(np.linalg.norm(user_stroke - point, axis=1))
#         distances.append(min_distance)
#     # Return the average of the minimum distances
#     return np.mean(distances)
#
#
# def find_closest_stroke(user_stroke, dataset, tolerance=0.1):
#     closest_stroke = None
#     closest_distance = float('inf')
#
#     for original in dataset:
#         distance = calculate_distance(user_stroke, original)
#         if distance < closest_distance and distance <= tolerance:
#             closest_distance = distance
#             closest_stroke = original
#
#     if closest_stroke is None:
#         # Suggest the closest one regardless of tolerance
#         for original in dataset:
#             distance = calculate_distance(user_stroke, original)
#             if distance < closest_distance:
#                 closest_distance = distance
#                 closest_stroke = original
#
#     return closest_stroke
#
#
# # Example user input stroke
# user_input_stroke = np.array([[0, 0], [0.5, 0.5]])  # Modify as needed
#
# # Load your dataset
# loaded_dataset = np.load('shapes_and_lines_dataset.npy', allow_pickle=True)
#
# # Find the closest stroke
# closest_stroke = find_closest_stroke(user_input_stroke, loaded_dataset)
#
# if closest_stroke is not None:
#     print("Suggested Stroke:", closest_stroke)
# else:
#     print("No suitable stroke found.")


# import numpy as np
#
# def calculate_distance(stroke1, stroke2):
#     stroke1 = np.array(stroke1)
#     stroke2 = np.array(stroke2)
#     min_length = min(len(stroke1), len(stroke2))
#     distance = np.sum(np.linalg.norm(stroke1[:min_length] - stroke2[:min_length], axis=1))
#     return distance
#
# def find_closest_strokes(user_stroke, dataset, tolerance=0.5, num_suggestions=4):
#     closest_strokes = []
#
#     for original in dataset:
#         distance = calculate_distance(original, user_stroke)
#
#         if distance <= tolerance:
#             closest_strokes.append(original)
#             if len(closest_strokes) >= num_suggestions:
#                 break
#
#     # Ensure we have enough suggestions
#     while len(closest_strokes) < num_suggestions:
#         random_stroke = dataset[np.random.randint(len(dataset))]
#         # Convert strokes to tuple for comparison
#         if not any(np.array_equal(random_stroke, cs) for cs in closest_strokes):
#             closest_strokes.append(random_stroke)
#
#     return closest_strokes
#
# # Example usage
# user_input_stroke = np.array([[0, 0], [1, 1]])  # Replace with actual user input
# loaded_dataset = np.load('shapes_lines_abstract_dataset.npy', allow_pickle=True)
#
# closest_strokes = find_closest_strokes(user_input_stroke, loaded_dataset)
# print("Suggested Strokes:", closest_strokes)

# suggestion.py
import numpy as np

def calculate_distance(stroke1, stroke2):
    stroke1 = np.array(stroke1)
    stroke2 = np.array(stroke2)
    min_length = min(len(stroke1), len(stroke2))
    distance = np.sum(np.linalg.norm(stroke1[:min_length] - stroke2[:min_length], axis=1))
    return distance

def find_closest_strokes(user_stroke, dataset, tolerance=0.5, num_suggestions=4):
    closest_strokes = []

    for original in dataset:
        distance = calculate_distance(original, user_stroke)

        if distance <= tolerance:
            closest_strokes.append(original)
            if len(closest_strokes) >= num_suggestions:
                break

    # Ensure we have enough suggestions
    while len(closest_strokes) < num_suggestions:
        random_stroke = dataset[np.random.randint(len(dataset))]
        # Convert strokes to tuple for comparison
        if not any(np.array_equal(random_stroke, cs) for cs in closest_strokes):
            closest_strokes.append(random_stroke)

    return closest_strokes


