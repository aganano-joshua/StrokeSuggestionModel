import numpy as np
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


# Load the Quick, Draw! dataset
def load_quick_draw_data(category):
    file_path = f'dataset/{category}.npz'
    if not os.path.exists(file_path):
        print(f"Data file not found: {file_path}")
        return []

    with np.load(file_path, allow_pickle=True) as data:  # Allow loading object arrays
        print(f"Loaded data for category: {category}")
        return data['train']  # Load the training data


# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    print(f"Calculating distance between:\nPoint1: {point1}\nPoint2: {point2}")

    # If point1 has more dimensions, reduce it to match point2
    if point1.shape[0] > point2.shape[0]:
        print("Point1 has more points, trimming to match Point2.")
        point1 = point1[:point2.shape[0]]  # Take only the first N points of point1

    # If point2 has more dimensions, reduce it to match point1
    elif point2.shape[0] > point1.shape[0]:
        print("Point2 has more points, trimming to match Point1.")
        point2 = point2[:point1.shape[0]]  # Take only the first N points of point2

    distance = np.sqrt(np.sum((point1 - point2) ** 2))
    print(f"Distance calculated: {distance}")
    return distance


# Suggest similar drawings based on user input
def suggest_similar_drawings(user_drawing, category_data, num_suggestions=3):
    similarities = []
    user_points_count = len(user_drawing)
    print(f"User drawing has {user_points_count} points.")

    # Loop through each stored drawing in the category data
    for stored_drawing in category_data:
        stored_points_count = len(stored_drawing)
        print(f"Stored drawing has {stored_points_count} points.")

        # Compare user drawing to segments of the stored drawing
        for start in range(stored_points_count - user_points_count + 1):
            # Take a segment of the stored drawing that matches the length of the user drawing
            stored_segment = stored_drawing[start:start + user_points_count]
            print(f"Comparing with stored segment starting at {start}: {stored_segment}")

            # Ignore the third coordinate if it exists
            if stored_segment.shape[1] > 2:
                print("Trimming stored segment to 2 dimensions (x, y).")
                stored_segment = stored_segment[:, :2]  # Keep only x and y

            # Calculate the distance between user drawing and the current segment
            distance = euclidean_distance(np.array(user_drawing), np.array(stored_segment))
            similarities.append((stored_segment, distance))

    # Sort by distance (similarity)
    similarities.sort(key=lambda x: x[1])
    print(f"Top similarities: {similarities[:num_suggestions]}")

    # Get the top 'num_suggestions' similar drawings
    suggested_drawings = [drawing[0] for drawing in similarities[:num_suggestions]]
    print(f"Suggested drawings: {suggested_drawings}")

    return suggested_drawings


# Suggest coordinates based on user input shape
@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    print(f"Received request data: {data}")
    user_shape = data.get('shape')
    category = data.get('category')

    if not user_shape or not category:
        print("Invalid input: Shape or category missing.")
        return jsonify({'error': 'Invalid input'}), 400

    # Load the category data
    category_data = load_quick_draw_data(category)
    if not category_data:
        print(f"No data found for category: {category}")
        return jsonify({'error': 'No data found for this category'}), 404

    suggested_shapes = suggest_similar_drawings(user_shape, category_data)

    return jsonify({'suggestions': suggested_shapes.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
