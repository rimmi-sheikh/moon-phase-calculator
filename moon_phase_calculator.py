import ephem

def calculate_moon_phase(date_str):
    # Create an ephem.Date object for the specified date
    date = ephem.Date(date_str)

    # Compute the moon's phase for the given date
    moon_phase = ephem.Moon(date).phase

    # Determine the moon phase category
    if 0 <= moon_phase < 7.4:
        phase_category = "New Moon"
    elif 7.4 <= moon_phase < 14.8:
        phase_category = "First Quarter Waxing Crescent"
    elif 14.8 <= moon_phase < 22.1:
        phase_category = "First Quarter Waxing Gibbous"
    elif 22.1 <= moon_phase < 29.5:
        phase_category = "Full Moon"
    else:
        phase_category = "Unknown Phase"

    return phase_category

# Input date in YYYY-MM-DD format
input_date = "2023-09-20"
moon_phase_category = calculate_moon_phase(input_date)

print(f"The moon's phase on {input_date} is {moon_phase_category}.")

