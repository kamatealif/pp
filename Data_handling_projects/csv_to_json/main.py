import os 
import csv
import json

def load_csv(file_name):
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file {file_name} does not exist.")
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def convert_to_json(output_file, data):
    if not data:
        raise ValueError("No data to write to JSON file.")
    if not output_file.endswith('.json'):
        raise ValueError("Output file must have a .json extension.")
    with open(output_file, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"{len(data)} objects saved to {output_file}")
    

if __name__ == "__main__":
    FILE_NAME = 'data.csv'
    OUTPUT_FILE = 'output.json'

    
    try:
        data = load_csv(FILE_NAME)

        convert_to_json(OUTPUT_FILE, data)

    except Exception as e:
        print(f"An error occurred: {e}")