import os
from datetime import date

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
        if not date_str:
            return None
        parts = date_str.split('-')

        if len(parts) != 3:
            return None

        year_str, month_str, day_str = parts
        if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
            return None

        year, month, day = int(year_str), int(month_str), int(day_str)

        if month < 1 or month > 12:
            return None
        if day < 1 or day > 31:
            return None

        return date(year, month, day)

    def _to_int(self, value):
        if value and value.strip():
            return int(value)
        return None


class FileParser:
    def parse_file(self, file_path):
        weather_records = []
        if not os.path.exists(file_path):
            print(f"Error: File not found -> {file_path}")
            return weather_records
        if not os.path.isfile(file_path):
            print(f"Error: Path is not a file -> {file_path}")
            return weather_records

        with open(file_path, 'r') as file:
            # skip first header line
            next(file)
            for line in file:
                columns = line.strip().split(',')
                if not columns or len(columns) < 9:
                    continue
                reading = WeatherReading(
                    date_str=columns[0],
                    max_temp=columns[1],
                    min_temp=columns[3],
                    max_hum=columns[7],
                    mean_hum=columns[8]
                )
                if reading.date:
                    weather_records.append(reading)

        return weather_records
