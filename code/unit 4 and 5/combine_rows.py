from csv import DictReader

# Open and read the CSV file using the with statement
with open('../../data/unit 4 and 5/mn.csv', 'r') as f:
    mn_data_rdr = DictReader(f)
    mn_data = [d for d in mn_data_rdr]


def combine_data_dict(data_rows):
    data_dict = {}
    for row in data_rows:
        key = '%s-%s' % (row.get('HH1'), row.get('HH2'))
        if key in data_dict:
            data_dict[key].append(row)
        else:
            data_dict[key] = [row]
    return data_dict

mn_dict = combine_data_dict(mn_data)

print(len(mn_dict))
