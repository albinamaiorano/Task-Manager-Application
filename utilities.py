from datetime import datetime

def format_date(date):
    """
    Format a date string.

    Parameters:
    date (str): A string representing a date in the format "%Y-%m-%d %H:%M:%S".

    Returns:
    str: A formatted date string in the format "%B %d, %Y %I:%M %p".

    Raises:
    ValueError: If the input date string is not in the expected format.
    """
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        formatted_date = parsed_date.strftime("%B %d, %Y %I:%M %p")
        return formatted_date
    except ValueError:
        return "Invalid date format"
