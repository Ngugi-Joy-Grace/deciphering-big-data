from csv import DictReader

# Open and read the CSV files using the with statement
with open('../../data/unit 4 and 5/mn.csv', 'r') as f:
    data_rdr = DictReader(f)
    data_rows = [d for d in data_rdr]

with open('../../data/unit 4 and 5/mn_headers.csv', 'r') as f:
    header_rdr = DictReader(f)
    header_rows = [h for h in header_rdr]

# Create a mapping from the old header to the new header label
header_map = {}
for header_dict in header_rows:
    for key, value in header_dict.items():
        header_map[value] = header_dict.get('Label')

new_rows = []

for data_dict in data_rows:
    new_row = {}
    for dkey, dval in data_dict.items():
        if dkey in header_map:
            new_row[header_map[dkey]] = dval
    new_rows.append(new_row)

print(new_rows[0])
