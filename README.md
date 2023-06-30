# LIV2 - South African ID Number Validator

LIV2 is a simple Flask-based application that validates South African ID numbers and provides information extracted from them.

# Disclaimer
Please be advised that by default, this application is configured to run in debug mode, as specified in the run.py file. Debug mode facilitates active development of the application by providing detailed error messages and enabling features like hot reloading.

However, debug mode is not suitable for production environments due to potential security risks and performance issues. It can expose sensitive information in error messages, and it uses more system resources.

Before deploying this application in a production environment, ensure that debug mode is turned off. This can be done by setting `debug=False` in `run.py` or removing the `debug` parameter altogether since its default value is `False`.

Always ensure to follow best practices for deploying Flask applications in a production environment. Consult the [Flask Deployment Documentation](https://flask.palletsprojects.com/en/2.3.x/deploying/) for more detailed information.

## Features

- Validate South African ID numbers
- Extract date of birth, gender, nationality, and residency status from ID numbers

## Installation

Clone this repository.

	git clone https://github.com/calcanthum/liv2.git

Navigate to the project directory.

	cd liv2

Install the necessary dependencies.

	pip install -r requirements.txt

## Usage

Start the server by running:

	python run.py

This starts the server on `localhost` port `5000`.

You can then validate an ID number by making a POST request to `http://localhost:5000/validate_id` with a JSON payload like `{"id_number": "your_id_number"}`. Replace `"your_id_number"` with the actual ID number you want to validate.

For example, using `curl`, you can test the endpoint with the following command:

	curl -X POST -H "Content-Type: application/json" -d '{"id_number":"8205075432087"}' http://localhost:5000/validate_id
