import csv

# Function to read the CSV file and return a dictionary of VesselID to VesselName
def read_vessel_ids_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        vessel_dict = {}
        for row in reader:
            vessel_id = row['VesselId'].strip()
            vessel_name = row['Vessel Name'].strip()  # Now 'Vessel Name' should work
            vessel_dict[vessel_id] = vessel_name
        return vessel_dict

# Function to write the new Python file with comments
def write_python_file_with_comments(py_file_path, new_py_file_path, vessel_dict):
    with open(py_file_path, 'r') as pyfile:
        lines = pyfile.readlines()

    with open(new_py_file_path, 'w') as new_pyfile:
        for line in lines:
            if line.strip().endswith(','):
                vessel_id = line.split(',')[0].strip()
                vessel_name = vessel_dict.get(vessel_id, 'Unknown Vessel')
                new_pyfile.write(f"{line.rstrip()}  \t\t# {vessel_name}\n")
            else:
                new_pyfile.write(line)

# Replace 'your_csv_file_path.csv' and 'your_python_file_path.py' with your actual file paths
csv_file_path = ''
py_file_path = ''
new_py_file_path = 'y' # Or you can overwrite the original

# Read vessel IDs from CSV
vessel_dict = read_vessel_ids_from_csv(csv_file_path)

# Write new Python file with comments
write_python_file_with_comments(py_file_path, new_py_file_path, vessel_dict)

print(f"New Python file with comments written to {new_py_file_path}")
