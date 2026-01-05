from datetime import date


# A data structure to hold a single day's weather metrics.
class WeatherRecord:
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
            return

        parts = date_str.split("-")

        if len(parts) != 3:
            return

        year_str, month_str, day_str = parts
        if not (year_str.isdigit() and month_str.isdigit() and day_str.isdigit()):
            return

        year, month, day = int(year_str), int(month_str), int(day_str)

        if month < 1 or month > 12:
            return

        if day < 1 or day > 31:
            return

        return date(year, month, day)

    def _to_int(self, value):
        if value and value.strip():
            return int(value)

        return
