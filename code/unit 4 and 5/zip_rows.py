from csv import reader

# Open and read the CSV files using the with statement
with open('../../data/unit 4 and 5/mn.csv', 'r') as f:
    data_rdr = reader(f)
    data_rows = [d for d in data_rdr]

with open('../../data/unit 4 and 5/mn_headers.csv', 'r') as f:
    header_rdr = reader(f)
    header_rows = [h for h in header_rdr]

print(len(data_rows[0]))
print(len(header_rows))

bad_rows = []
for h in header_rows:
    if h[0] not in data_rows[0]:
        bad_rows.append(h)

for h in bad_rows:
    header_rows.remove(h)

print(len(header_rows))

all_short_headers = [h[0] for h in header_rows]
for header in data_rows[0]:
    if header not in all_short_headers:
        print('mismatch!', header)
