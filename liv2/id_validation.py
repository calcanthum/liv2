import datetime
import re

def validate_checksum(id_string: str) -> bool:
    """Validate the ID number using the Luhn algorithm."""
    evens = sum(int(i) for i in id_string[-1::-2])
    odds = sum(sum(divmod(int(i)*2, 10)) for i in id_string[-2::-2])
    return (evens + odds) % 10 == 0

# Use two different regex patterns, one for checking length and one for checking characters.
ID_NUMBER_LENGTH_REGEX = re.compile(r"^.{13}$")
ID_NUMBER_CHARS_REGEX = re.compile(r"^\d+$")

def validate_id(id_number: str) -> dict:
    """
    Validate South African ID number and provide extracted information.
    
    Parameters:
    id_number (str): The ID number to be validated.

    Returns:
    dict: A dictionary containing extracted information from the ID or an error message.
    """
    extracted_info = {}
    
    # Remove any spaces from the ID number.
    id_number = id_number.replace(" ", "")
    
    # Check ID number length
    if not ID_NUMBER_LENGTH_REGEX.match(id_number):
        extracted_info["error_message"] = "Invalid ID number length."
        return extracted_info
    
    # Check for non-digit characters
    if not ID_NUMBER_CHARS_REGEX.match(id_number):
        extracted_info["error_message"] = "Invalid characters found in ID number."
        return extracted_info

    # Validate check digit.
    if not validate_checksum(id_number):
        extracted_info["error_message"] = "Invalid check digit."
        return extracted_info

    # Extract birth date information.
    year_str = id_number[:2]
    month = int(id_number[2:4])
    day = int(id_number[4:6])

# Validate date
    try:
        # Handle dates from different centuries.
        current_year_suffix = datetime.datetime.now().year % 100  # last two digits of the current year
        year = int(year_str) + 2000 if int(year_str) <= current_year_suffix else int(year_str) + 1900

        date_of_birth = datetime.datetime(year, month, day)
    except ValueError:
        extracted_info["error_message"] = "Invalid date of birth."
        return extracted_info

    extracted_info["date_of_birth"] = date_of_birth.strftime('%Y-%m-%d')


    # Extract gender information.
    gender_indicator = int(id_number[6:10])
    extracted_info["gender"] = "Female" if gender_indicator < 5000 else "Male"

    # Extract nationality information.
    nationality_indicator = int(id_number[10])
    extracted_info["nationality"] = "South African" if nationality_indicator == 0 else "Immigrant"

    # Extract residence status information.
    residency_status_indicator = int(id_number[11])
    extracted_info["residency_status"] = "Citizen" if residency_status_indicator == 0 else "Resident"

    return extracted_info
