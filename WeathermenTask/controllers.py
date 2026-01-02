from utils import filter_by_month

class WeatherController:
    def __init__(self, analyzer, reporter):
        self.analyzer = analyzer
        self.reporter = reporter

    def run_yearly_summary(self, year, month, weather_data):
        high, low, humid = self.analyzer.get_yearly_stats(weather_data)
        self.reporter.print_yearly_summary(year, high, low, humid)

    def run_monthly_avg(self, year, month, weather_data):
        if not month:
            print("Error: Month is required for -a flag (e.g., 2004/3)")
            return
        monthly_data = filter_by_month(weather_data, month)
        if monthly_data:
            avg_max, avg_min, avg_hum = self.analyzer.get_monthly_averages(monthly_data)
            self.reporter.print_monthly_average(year, month, avg_max, avg_min, avg_hum)
        else:
            print(f"Warning: Data not found for {month}/{year}")

    def run_daily_temp_bars(self, year, month, weather_data):
        if not month:
            print("Error: Month is required for -c flag")
            return
        monthly_data = filter_by_month(weather_data, month)
        if monthly_data:
            self.reporter.draw_daily_temp_bars(year, month, monthly_data)
        else:
            print(f"Warning: Data not found for {month}/{year}")

    def run_temp_range_bar(self, year, month, weather_data):
        if not month:
            print("Error: Month is required for -b flag")
            return
        monthly_data = filter_by_month(weather_data, month)
        if monthly_data:
            self.reporter.draw_temp_range_chart(year, month, monthly_data)
        else:
            print(f"Warning: Data not found for {month}/{year}")
