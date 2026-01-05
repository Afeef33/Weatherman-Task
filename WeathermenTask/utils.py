import os

from weather_data import WeatherRecord


def parse_file(file_path):
    weather_records = []
    if not os.path.exists(file_path):
        print(f"Error: File not found -> {file_path}")

        return weather_records

    if not os.path.isfile(file_path):
        print(f"Error: Path is not a file -> {file_path}")

        return weather_records

    with open(file_path, "r") as file:
        # skip first header line
        next(file)
        for line in file:
            columns = line.strip().split(",")
            if not columns or len(columns) < 9:
                continue

            reading = WeatherRecord(
                date_str=columns[0],
                max_temp=columns[1],
                min_temp=columns[3],
                max_hum=columns[7],
                mean_hum=columns[8],
            )

            if reading.date:
                weather_records.append(reading)

    return weather_records


def print_extreme(label, weather_record, attr_name, unit):
    if weather_record:
        value = getattr(weather_record, attr_name)
        date_str = weather_record.date.strftime("%B %d")
        print(f"{label}: {value}{unit} on {date_str}")
    else:
        print(f"{label}: Data not available")


def find_extreme(weather_records, attr_name, find_max=True):
    valid_records = [r for r in weather_records if getattr(r, attr_name) is not None]
    if not valid_records:
        return None

    if find_max:
        return max(valid_records, key=lambda r: getattr(r, attr_name))

    else:
        return min(valid_records, key=lambda r: getattr(r, attr_name))


def calculate_avg(readings, attr_name):
    values = [
        getattr(r, attr_name) for r in readings if getattr(r, attr_name) is not None
    ]
    if not values:
        return 0

    return sum(values) // len(values)


def get_year_files(directory, year):
    file_paths = []
    if not os.path.exists(directory):
        print(f"Error: Folder not found -> {directory}")

        return []

    for filename in os.listdir(directory):
        if year in filename and filename.endswith(".txt"):
            full_path = os.path.join(directory, filename)
            file_paths.append(full_path)

    return file_paths


def filter_by_month(readings, month):
    return [r for r in readings if r.date.month == int(month)]


def print_usage():
    print(
        """
    Weatherman CLI Tool - Usage Guide
    ---------------------------------
    python weatherman.py <path> <flag> <date>

    Flags:
      -e <year>       : Yearly Report (Highest/Lowest Temp, Humidity)
      -a <year/month> : Monthly Averages
      -c <year/month> : Horizontal Charts (Daily Bars)
      -b <year/month> : Bonus Chart (Temp Range)

    Example:
      python weatherman.py weather_files -e 2004
      python weatherman.py weather_files -a 2004/3
      python weatherman.py weather_files -c 2004/3
      python weatherman.py weather_files -b 2004/3
    """
    )

