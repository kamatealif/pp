import json 
import csv
import os


def load_json_data(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"The file {file} does not exist.")
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file {file}: {e}")

def conver_to_csv(data, output_file):
    if not data:
        print("No data to write to CSV.")
    headers = list(data[0].keys())
    row_count =0
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader();
        for row in data:
            writer.writerow(row)
            row_count += 1
    print(f"Total rows written: {row_count}")
    print(f"Data successfully written to {output_file}")

if __name__ == "__main__":
    # Define the path to the JSON file
    FILE_NAME   = "api_data.json"
    OUTPUT_FILE = "converted_data.csv"
    print("Starting the conversion of JSON to CSV process...")
    try:
        # Load JSON data
        json_data = load_json_data(FILE_NAME)
        # Convert to CSV
        conver_to_csv(json_data, OUTPUT_FILE)
    except Exception as e:
        print(f"An error occurred: {e}")
        