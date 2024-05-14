from datetime import datetime

def format_date(date):
    """Format a date string."""
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        formatted_date = parsed_date.strftime("%B %d, %Y %I:%M %p")
        return formatted_date
    except ValueError:
        return "Invalid date format"
