# LIV2 - South African ID Number Validator

LIV2 is a simple Flask-based application that validates South African ID numbers and provides information extracted from them.

## Features

- Validate South African ID numbers
- Extract date of birth, gender, nationality, and residency status from ID numbers

## Installation

1. Clone this repository.

	git clone https://github.com/calcanthum/liv2.git

2. Navigate to the project directory.

	cd liv2

3. Install the necessary dependencies.

	pip install -r requirements.txt

## Usage

Start the server by running:

	python run.py

This starts the server on `localhost` port `5000`.

You can then validate an ID number by making a POST request to `http://localhost:5000/validate_id` with a JSON payload like `{"id_number": "your_id_number"}`. Replace `"your_id_number"` with the actual ID number you want to validate.

For example, using `curl`, you can test the endpoint with the following command:

curl -X POST -H "Content-Type: application/json" -d '{"id_number":"8205075432087"}' http://localhost:5000/validate_id

