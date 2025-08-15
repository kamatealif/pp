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
    
def show_data(data, preview_count = 5):
    if not data:
        print("No data to display.")
    else:

        print(f"Displaying first {preview_count} records:")
        for i, record in enumerate(data[:preview_count]):
            print(f"Record {1 + 1} : {record}")
    

if __name__ == "__main__":
    FILE_NAME = 'data.csv'
    OUTPUT_FILE = 'output.json'

    
    try:
        data = load_csv(FILE_NAME)

        convert_to_json(OUTPUT_FILE, data)

        choice = input("Do you want to preview the data? (yes/no): ").strip().lower()
        if choice == 'yes' or choice == 'y':
            preview_count = int(input("How many records would you like to preview? "))
            show_data(data, preview_count)
        else:
            print("Preview skipped.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as ve:
        print(ve)

    except Exception as e:
        print(f"An error occurred: {e}")