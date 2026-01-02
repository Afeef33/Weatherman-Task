
class WeatherAnalyzer:


    def get_yearly_stats(self, readings):

        # Step 1: Clean Data
        valid_max_temps = [r for r in readings if r.max_temp is not None]
        valid_min_temps = [r for r in readings if r.min_temp is not None]
        valid_humidity = [r for r in readings if r.max_humidity is not None]

        highest = None
        lowest = None
        most_humid = None

        # Step 2: Finding requirements
        if valid_max_temps:
            highest = max(valid_max_temps, key=lambda r: r.max_temp)

        if valid_min_temps:
            lowest = min(valid_min_temps, key=lambda r: r.min_temp)

        if valid_humidity:
            most_humid = max(valid_humidity, key=lambda r: r.max_humidity)

        return highest, lowest, most_humid

    def get_monthly_averages(self, readings):

        # Step 1: Cleaning
        max_temps = [r.max_temp for r in readings if r.max_temp is not None]
        min_temps = [r.min_temp for r in readings if r.min_temp is not None]
        mean_humidity = [r.mean_humidity for r in readings if r.mean_humidity is not None]

        # Step 2: Calculation
        avg_max = sum(max_temps) // len(max_temps) if max_temps else 0
        avg_min = sum(min_temps) // len(min_temps) if min_temps else 0
        avg_humid = sum(mean_humidity) // len(mean_humidity) if mean_humidity else 0

        return avg_max, avg_min, avg_humid