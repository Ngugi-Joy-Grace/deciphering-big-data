from csv import reader

# Open and read the CSV files using the with statement
with open('../../data/unit 4 and 5/mn.csv', 'r') as f:
    data_rdr = reader(f)
    data_rows = [d for d in data_rdr]

with open('../../data/unit 4 and 5/mn_headers_updated.csv', 'r') as f:
    header_rdr = reader(f)
    header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

print(len(header_rows))

all_short_headers = [h[0] for h in header_rows]
skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

del all_short_headers

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

zipped_data = []

for drow in new_data:
    zipped_data.append(list(zip(final_header_rows, drow)))

print(zipped_data[0])
