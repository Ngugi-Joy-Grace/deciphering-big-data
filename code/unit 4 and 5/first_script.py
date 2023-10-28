from csv import reader
import dataset

# Open and read the CSV files using the with statement
with open('../../data/unit 4 and 5/mn.csv', 'r') as f:
    data_rdr = reader(f)
    data_rows = [d for d in data_rdr]

with open('../../data/unit 4 and 5/mn_headers_updated.csv', 'r') as f:
    header_rdr = reader(f)
    header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

all_short_headers = [h[0] for h in header_rows]

skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        print(header)
        index = data_rows[0].index(header)
        if index not in skip_index:
            skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = [d for i, d in enumerate(row) if i not in skip_index]
    new_data.append(new_row)

zipped_data = [list(zip(final_header_rows, drow)) for drow in new_data]

# Look for missing values
for x in zipped_data[0]:
    if not x[1]:
        print(x)

# Look for dupes
set_of_keys = {'%s-%s-%s' % (x[0][1], x[1][1], x[2][1]) for x in zipped_data}
uniques = [x for x in zipped_data if '%s-%s-%s' % (x[0][1], x[1][1], x[2][1]) in set_of_keys]

print(len(set_of_keys))

# Saving to db
db = dataset.connect('sqlite:///../../data_wrangling.db')
table = db['unicef_survey']

for row_num, data in enumerate(zipped_data):
    for question, answer in data:
        data_dict = {
            'question': question[1],
            'question_code': question[0],
            'answer': answer,
            'response_number': row_num,
            'survey': 'mn',
        }
        table.insert(data_dict)
