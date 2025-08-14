Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:

1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:

- Format the output like a table
- Handle API failures and invalid city names gracefully

## how to run file

first make sure to make an account at `https://home.openweathermap.org/` and create your api

```bash
pip install uv
```

install all the required dependencies

```bash
uv sync
```

create a .env file and inside .env add one var `API_KEY=<YOUR_API_KEY>`

Run the Script:

```bash
uv run main.py
```
