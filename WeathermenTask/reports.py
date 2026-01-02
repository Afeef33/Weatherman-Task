
class ReportGenerator:


    # ANSI Color Codes
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    def print_yearly_summary(self, year, high, low, humid):
        print(f"\n=== Yearly Report for {year} ===")
        if high:
            print(f"Highest: {high.max_temp}C on {high.date.strftime('%B %d')}")
        else:
            print("Highest: Data not available")

        if low:
            print(f"Lowest: {low.min_temp}C on {low.date.strftime('%B %d')}")
        else:
            print("Lowest: Data not available")

        if humid:
            print(f"Humidity: {humid.max_humidity}% on {humid.date.strftime('%B %d')}")
        else:
            print("Humidity: Data not available")

    def print_monthly_average(self, year, month, avg_max, avg_min, avg_hum):
        print(f"\n=== Monthly Report for {month}/{year} ===")
        print(f"Highest Average: {avg_max}C")
        print(f"Lowest Average: {avg_min}C")
        print(f"Average Mean Humidity: {avg_hum}%")

    def draw_charts(self, year, month, readings):

        print(f"\n=== Temperature Charts for {month}/{year} ===")

        for reading in readings:
            if reading.max_temp is None or reading.min_temp is None:
                continue

            day_number = reading.date.day

            # RED BAR (Max Temp)
            print(f"{day_number:02d} {self.RED}{'+' * reading.max_temp}{self.RESET} {reading.max_temp}C")

            # BLUE BAR (Min Temp)
            print(f"{day_number:02d} {self.BLUE}{'+' * reading.min_temp}{self.RESET} {reading.min_temp}C")

    def draw_bonus_chart(self, year, month, readings):

        print(f"\n=== Bonus Combined Chart for {month}/{year} ===")

        for reading in readings:
            if reading.max_temp is None or reading.min_temp is None:
                continue

            day_number = reading.date.day
            blue_pluses = reading.min_temp
            red_pluses = reading.max_temp - reading.min_temp

            print(
                f"{day_number:02d} {self.BLUE}{'+' * blue_pluses}{self.RED}{'+' * red_pluses}{self.RESET} {reading.min_temp}C - {reading.max_temp}C")