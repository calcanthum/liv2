import datetime
import re

def validate_checksum(id_string: str) -> bool:
    """Validate the ID number using the Luhn algorithm."""
    evens = sum(int(i) for i in id_string[-1::-2])
    odds = sum(sum(divmod(int(i)*2, 10)) for i in id_string[-2::-2])
    return (evens + odds) % 10 == 0

def validate_id(id_number: str) -> dict:
    """
    Validate South African ID number and provide extracted information.
    
    Parameters:
    id_number (str): The ID number to be validated.

    Returns:
    dict: A dictionary containing extracted information from the ID or an error message.
    """
    extracted_info = {}

    # Ensure ID number format with a regular expression.
    if not re.match(r"\d{13}$", id_number):
        extracted_info["error_message"] = "Invalid ID number length or non-digit characters found."
        return extracted_info

    # Validate check digit.
    if not validate_checksum(id_number):
        extracted_info["error_message"] = "Invalid check digit."
        return extracted_info

    # Extract birth date information.
    date_of_birth_str = id_number[:6]
    year = int(date_of_birth_str[:2])
    month = int(date_of_birth_str[2:4])
    day = int(date_of_birth_str[4:6])

    # Validate date
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        extracted_info["error_message"] = "Invalid date of birth."
        return extracted_info


    # Handle dates from different centuries.
    current_year = datetime.datetime.now().year
    current_year_suffix = current_year % 100  # last two digits of the current year
    year += 2000 if year <= current_year_suffix else 1900

    # List of month names for conversion
    month_names = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]

    extracted_info["date_of_birth"] = f"{day} {month_names[month-1]} {year}"

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
