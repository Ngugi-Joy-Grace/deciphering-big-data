import slate3k as slate

pdf = '../../data/unit 1/EN-FINAL Table 9.pdf'

with open(pdf, 'rb') as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print(type(page).__name__)
