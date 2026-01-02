from utils import find_extreme, calculate_avg

class WeatherAnalyzer:
    def get_yearly_stats(self, weather_records):
        max_temp = find_extreme(weather_records, 'max_temp', find_max=True)
        min_temp = find_extreme(weather_records, 'min_temp', find_max=False)
        max_humid = find_extreme(weather_records, 'max_humidity', find_max=True)

        return max_temp, min_temp, max_humid

    def get_monthly_averages(self, weather_records):
        avg_max_temp = calculate_avg(weather_records, 'max_temp')
        avg_min_temp = calculate_avg(weather_records, 'min_temp')
        avg_humid = calculate_avg(weather_records, 'mean_humidity')

        return avg_max_temp, avg_min_temp, avg_humid
