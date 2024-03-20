import pandas as pd
import json

# Load nested JSON data from a file
with open('nested_data.json', 'r') as json_file:
    nested_json_data = json.load(json_file)

# Function to flatten nested JSON data
def flatten_json(json_data, parent_key='', separator='_'):
    items = {}
    for key, value in json_data.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, separator))
        else:
            items[new_key] = value
    return items

# Flatten the nested JSON data
flattened_data = [flatten_json(data) for data in nested_json_data.values()]

# Convert flattened data to DataFrame
df = pd.DataFrame(flattened_data)

# Convert DataFrame to Excel
excel_file_path = 'nested_data.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Excel file '{excel_file_path}' has been created.")
