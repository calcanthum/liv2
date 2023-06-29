from flask import Blueprint, request, jsonify
from .id_validation import validate_id

main = Blueprint('main', __name__)

@main.route('/validate_id', methods=['POST'])
def validate_id_endpoint():
    data = request.get_json()
    id_number = data.get('id_number', '')
    result = validate_id(id_number)
    return jsonify(result), 200
