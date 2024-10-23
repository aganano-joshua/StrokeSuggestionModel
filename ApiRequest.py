# app.py
from flask import Flask, request, jsonify
import numpy as np
from suggest import find_closest_strokes  # Import your suggestion function

app = Flask(__name__)

# Load your dataset
loaded_dataset = np.load('shapes_lines_abstract_dataset.npy', allow_pickle=True)


@app.route('/suggest', methods=['POST'])
def suggest():
    """API endpoint to suggest strokes based on user input."""
    data = request.json
    user_stroke = np.array(data['stroke'])  # Expecting a stroke in the format [[x1, y1], [x2, y2], ...]

    closest_strokes = find_closest_strokes(user_stroke, loaded_dataset)

    # Convert closest strokes to a list of lists for JSON response
    response = [stroke.tolist() for stroke in closest_strokes]

    return jsonify({'suggestions': response})


if __name__ == '__main__':
    app.run(debug=True)
