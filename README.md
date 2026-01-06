# Weatherman CLI Tool 🌦️

A Python-based command-line tool to analyze weather data.

## Features
- **Yearly Summary Report:** Get highest/lowest temperatures (`-e`).
- **Monthly Average Report:** Get average stats (`-a`).
- **Daily Temperature Chart:** Visual bar charts for temperatures (`-c`).
- **Combined Daily Bar Chart:** Bar combining both the high and low temperatures (`-b`).

## Usage
```bash
python weatherman.py weather_files -e 2004
python weatherman.py weather_files -a 2004/3
python weatherman.py weather_files -c 2004/3
