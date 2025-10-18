import os 

file_count =0;

file_path = 'folder path here'

for dirpath, dirnames, filenames in os.walk(file_path):
    print(f'Found directory: {dirpath}')
    
    for filename in filenames:
        if filename.endswith('.java'):
            file_count += 1
            
print(f'Total .java files: {file_count}')