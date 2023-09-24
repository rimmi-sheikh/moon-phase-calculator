import datetime

def calculate_moon_phase(date_str):
    try:
        # Convert the input date to a datetime object
        input_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        # Known new moon date (January 1, 2023)
        new_moon_date = datetime.datetime(2023, 1, 1)

        # Calculate the number of days between the input date and the known new moon date
        delta = input_date - new_moon_date

        # Calculate the moon's age using a more precise value for the number of days in a lunar month
        lunar_month_days = 29.53058867  # The precise value

        # Calculate the moon's age
        moon_age = delta.days % lunar_month_days

        # Determine the moon phase category
        if 0 <= moon_age < 7.4:
            phase_category = "New Moon"
        elif 7.4 <= moon_age < 14.8:
            phase_category = "First Quarter Waxing Crescent"
        elif 14.8 <= moon_age < 22.1:
            phase_category = "First Quarter Waxing Gibbous"
        elif 22.1 <= moon_age < 29.5:
            phase_category = "Full Moon"
        else:
            phase_category = "Unknown Phase"

        return phase_category

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Input date in YYYY-MM-DD format
    input_date = input("Enter a date (YYYY-MM-DD): ")

    moon_phase_category = calculate_moon_phase(input_date)

    if moon_phase_category != "Unknown Phase":
        print(f"The moon's phase on {input_date} is {moon_phase_category}.")
    else:
        print(f"Unable to determine the moon's phase for {input_date}. Please check the date format (YYYY-MM-DD).")
