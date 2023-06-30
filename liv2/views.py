from flask import Blueprint, request, jsonify
from .id_validation import validate_id

main = Blueprint('main', __name__)

@main.route('/validate_id', methods=['POST'])
def validate_id_endpoint():
    data = request.get_json()

    if not data or 'id_number' not in data:
        return jsonify({"error_message": "Invalid request. No 'id_number' key found in JSON data."}), 400

    id_number = data.get('id_number', '')
    result = validate_id(id_number)
    return jsonify(result), 200
