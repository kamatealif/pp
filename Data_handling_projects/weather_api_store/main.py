import os 
import requests
from datetime import datetime
import csv
from dotenv import load_dotenv
from collections import Counter

def log_weather(api,file_name):
    city = input("Enter City name: ")
    date = datetime.now().strftime("%d-%m-%Y")
    with open(file_name,'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Date'] == date and row['City'].lower() == city.lower():
                print("Entry for this city and date exists")
                return
    try:
        uri = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
        
        response = requests.get(url=uri)
        data = response.json()

        if response.status_code != 200:
            print(f"API Eror: {data.get('message')}")
            return
        
        temprature = data['main']['temp'] - 273.15
        condition = data['weather'][0]['main']

        with open(file_name,'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow([date,city,temprature,condition])
           
        
            print(f"Weather Logged: {city} on {date} : {temprature} : {condition}")


    except Exception as e:
        print("Error: ", e)

def show_all_weather(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        if len(reader) <=1:
            print("No weather data found.")
        for row in reader:
            print(f"Date: {row[0]}\nCity: {row[1]}\nTemprature: {row[2]}\nCondition: {row[3]}\n")

def calculate_statistics(filename):
    temperatures = []
    conditions = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            temperatures.append(float(row[2]))
            conditions.append(row[3])

    average_temperature = sum(temperatures) / len(temperatures)
    highest_temperature = max(temperatures)
    lowest_temperature = min(temperatures)
    most_frequent_condition = Counter(conditions).most_common(1)[0][0]

    print(f"Average Temperature: {average_temperature:.2f}°C")
    print(f"Highest Temperature: {highest_temperature}°C")
    print(f"Lowest Temperature: {lowest_temperature}°C")
    print(f"Most Frequent Condition: {most_frequent_condition}")


def show_menu():
    print("Menu:")
    print("1. Log Weather")
    print("2. View all weather data")
    print("3. Calculate statistics")
    print("4. Exit")
    print()

if __name__ == "__main__":
    load_dotenv();

    API_KEY = os.getenv("API_KEY")
    FILE_NAME = "weather_data.csv"
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'City', 'Temprature', 'Condition'])

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            log_weather(API_KEY, FILE_NAME)
        elif choice == "2":
            show_all_weather(FILE_NAME)
        elif choice == "3":
            calculate_statistics(FILE_NAME)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")