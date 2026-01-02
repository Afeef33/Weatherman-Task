# models.py
from datetime import datetime


class WeatherReading:
    def __init__(self, date_str, max_temp, min_temp, max_hum, mean_hum):
        self.date = self._parse_date(date_str)
        # Temperatures
        self.max_temp = self._to_int(max_temp)
        self.min_temp = self._to_int(min_temp)
        # Humidity
        self.max_humidity = self._to_int(max_hum)
        self.mean_humidity = self._to_int(mean_hum)

    def _parse_date(self, date_str):
        try:
            # File format is'2004-8-1'
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return None

    def _to_int(self, value):
        if value and value.strip():
            return int(value)
        return None


# --- PARSER CLASS ---

class FileParser:
    def parse_file(self, file_path):

        readings = []

        try:
            with open(file_path, 'r') as file:
                # skip first header line
                next(file)

                for line in file:
                    parts = line.strip().split(',')

                    if not parts or len(parts) < 9:
                        continue

                    # Specific Columns
                    reading = WeatherReading(
                        date_str=parts[0],
                        max_temp=parts[1],
                        min_temp=parts[3],
                        max_hum=parts[7],
                        mean_hum=parts[8]
                    )

                    if reading.date:
                        readings.append(reading)

        except FileNotFoundError:
            print(f"Error: File not found -> {file_path}")

        return readings