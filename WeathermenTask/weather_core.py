from utils import calculate_avg, filter_by_month, find_extreme, print_extreme


# Responsible for all visual output, including text reports and charts.
class WeatherReportGenerator:
    # ANSI Color Codes
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    def print_yearly_summary(self, year, high, low, humid):
        print(f"\n=== Yearly Report for {year} ===")
        print_extreme("Highest", high, 'max_temp', 'C')
        print_extreme("Lowest", low, 'min_temp', 'C')
        print_extreme("Humidity", humid, 'max_humidity', '%')

    def print_monthly_average(self, year, month, stats):
        print(f"\n=== Monthly Report for {month}/{year} ===")
        print(f"Highest Average: {stats['avg_max']}C")
        print(f"Lowest Average: {stats['avg_min']}C")
        print(f"Average Mean Humidity: {stats['avg_humid']}%")

    def draw_daily_temp_bars(self, year, month, readings):
        print(f"\n=== Temperature Charts for {month}/{year} ===")
        for reading in readings:
            if reading.max_temp is None or reading.min_temp is None:
                continue

            # Red Bar (Max Temp)
            print(f"{reading.date.day:02d} {self.RED}{'+' * reading.max_temp}{self.RESET} {reading.max_temp}C")
            # Blue Bar (Min Temp)
            print(f"{reading.date.day:02d} {self.BLUE}{'+' * reading.min_temp}{self.RESET} {reading.min_temp}C")

    def draw_temp_range_chart(self, year, month, readings):
        print(f"\n=== Bonus Combined Chart for {month}/{year} ===")

        for reading in readings:
            if reading.max_temp is None or reading.min_temp is None:
                continue

            blue_pluses = reading.min_temp
            red_pluses = reading.max_temp - reading.min_temp

            print(
                f"{reading.date.day:02d} "
                f"{self.BLUE}{'+' * blue_pluses}"
                f"{self.RED}{'+' * red_pluses}{self.RESET} "
                f"{reading.min_temp}C - {reading.max_temp}C"
            )


# Processes weather data and triggers the correct report display.
class WeatherManager:
    def __init__(self, report_generator):
        self.report_generator = report_generator

    def _get_monthly_data(self, year, month, weather_data, flag_name):
        if not month:
            print(f"Error: Month is required for {flag_name}")

            return None

        monthly_data = filter_by_month(weather_data, month)

        if not monthly_data:
            print(f"Warning: Data not found for {month}/{year}")

            return None

        return monthly_data

    def calculate_yearly_stats(self, weather_records):
        max_temp = find_extreme(weather_records, 'max_temp', find_max=True)
        min_temp = find_extreme(weather_records, 'min_temp', find_max=False)
        max_humid = find_extreme(weather_records, 'max_humidity', find_max=True)

        return max_temp, min_temp, max_humid

    def calculate_monthly_averages(self, weather_records):
        avg_max_temp = calculate_avg(weather_records, 'max_temp')
        avg_min_temp = calculate_avg(weather_records, 'min_temp')
        avg_humid = calculate_avg(weather_records, 'mean_humidity')

        return avg_max_temp, avg_min_temp, avg_humid

    def get_yearly_summary(self, year, month, weather_data):
        high, low, humid = self.calculate_yearly_stats(weather_data)
        self.report_generator.print_yearly_summary(year, high, low, humid)

    def get_monthly_avg(self, year, month, weather_data):
        monthly_data = self._get_monthly_data(
            year, month, weather_data, "-a flag"
        )

        if monthly_data:
            avg_max, avg_min, avg_hum = self.calculate_monthly_averages(monthly_data)

            stats={
                "avg_max" : avg_max,
                "avg_min" : avg_min,
                "avg_humid" : avg_hum
            }

            self.report_generator.print_monthly_average(year, month, stats)

    def get_daily_temp_bars(self, year, month, weather_data):
        monthly_data = self._get_monthly_data(
            year, month, weather_data, "-c flag"
        )

        if monthly_data:
            self.report_generator.draw_daily_temp_bars(year, month, monthly_data)

    def get_temp_range_bar(self, year, month, weather_data):
        monthly_data = self._get_monthly_data(
            year, month, weather_data, "-b flag"
        )

        if monthly_data:
            self.report_generator.draw_temp_range_chart(year, month, monthly_data)
