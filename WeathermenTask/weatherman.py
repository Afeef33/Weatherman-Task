import sys
import os
from models import FileParser
from utils import WeatherAnalyzer
from reports import ReportGenerator


def get_year_files(directory, year):

    file_paths = []

    # Folder check
    if not os.path.exists(directory):
        print(f"Error: Folder not found -> {directory}")
        return []

    # Files to parse
    for filename in os.listdir(directory):
        if year in filename and filename.endswith(".txt"):
            full_path = os.path.join(directory, filename)
            file_paths.append(full_path)

    return file_paths


def filter_by_month(readings, month):
    return [r for r in readings if r.date.month == int(month)]


def main():
    if len(sys.argv) < 3:
        print("Usage: python weatherman.py /path/to/files -e 2004")
        return

    folder_path = sys.argv[1]

    parser = FileParser()
    analyzer = WeatherAnalyzer()
    reporter = ReportGenerator()

    # Loop for arguments
    for i in range(2, len(sys.argv), 2):
        flag = sys.argv[i]
        date_arg = sys.argv[i + 1]

        if '/' in date_arg:
            year, month = date_arg.split('/')
        else:
            year = date_arg
            month = None

        # --- STEP 1: LOAD ALL DATA FOR THE YEAR ---
        year_files = get_year_files(folder_path, year)

        if not year_files:
            print(f"Error: Year {year} file(s) not found!")
            continue

        # Putting all months data in a single list
        all_readings = []
        for file_path in year_files:
            # use extend as append will add list
            all_readings.extend(parser.parse_file(file_path))

        # --- STEP 2: GENERATE REPORTS ---

        # Case 1: Yearly Report (-e)
        if flag == '-e':
            high, low, humid = analyzer.get_yearly_stats(all_readings)
            reporter.print_yearly_summary(year, high, low, humid)

        # Case 2: Monthly Average (-a)
        elif flag == '-a':
            if month:
                # data of required month from all_reading list
                monthly_data = filter_by_month(all_readings, month)
                if monthly_data:
                    avg_max, avg_min, avg_hum = analyzer.get_monthly_averages(monthly_data)
                    reporter.print_monthly_average(year, month, avg_max, avg_min, avg_hum)
                else:
                    print(f"Warning: Month {month} data not found.")
            else:
                print("month number is required in the argument")
        # Case 3: Charts (-c)
        elif flag == '-c':
            if month:
                monthly_data = filter_by_month(all_readings, month)
                if monthly_data:
                    reporter.draw_charts(year, month, monthly_data)
                else:
                    print(f"Warning: Month {month} data not found.")
            else:
                print("month number is required in the argument")
        elif flag == '-b':
            if month:
                monthly_data = filter_by_month(all_readings, month)
                if monthly_data:
                    reporter.draw_bonus_chart(year, month, monthly_data)
                else:
                    print(f"Warning: Month {month} data not found.")
            else:
                print("month number is required in the argument")
        else:
            print("flag not recognized")
if __name__ == "__main__":
    main()