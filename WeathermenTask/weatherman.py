import sys

from parsers import FileParser
from weather_cores import WeatherController, WeatherAnalyzer, ReportGenerator
from utils import get_year_files,print_usage


def main():
    folder_path = sys.argv[1]

    parser = FileParser()
    analyzer = WeatherAnalyzer()
    reporter = ReportGenerator()
    controller = WeatherController(analyzer, reporter)

    actions = {
        '-e': controller.run_yearly_summary,
        '-a': controller.run_monthly_avg,
        '-c': controller.run_daily_temp_bars,
        '-b': controller.run_temp_range_bar
    }

    # Loop for arguments
    for i in range(2, len(sys.argv), 2):
        flag = sys.argv[i]
        if i + 1 >= len(sys.argv):
            print(f"Error: Missing date argument for flag '{flag}'")
            break

        date_arg = sys.argv[i + 1]

        # Check Action Validity
        action_func = actions.get(flag)
        if not action_func:
            print(f"Error: Unknown flag '{flag}'")
            continue

        if '/' in date_arg:
            year, month = date_arg.split('/')
        else:
            year = date_arg
            month = None

        year_files = get_year_files(folder_path, year)
        if not year_files:
            print(f"Error: Year {year} file(s) not found!")
            continue

        weather_reports = []
        for file_path in year_files:
            weather_reports.extend(parser.parse_file(file_path))

        action_func(year=year, month=month, weather_data=weather_reports)


if __name__ == "__main__":
    if "--help" in sys.argv:
        print_usage()
        sys.exit()

    if len(sys.argv) < 4:
        print("Invalid arguments.")
        print_usage()
        sys.exit()
