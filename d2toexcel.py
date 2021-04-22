import pandas as pd

print('This script convert HTML file with table to XLSX file.')
name = input('Type name for Excel file:\n')
url = input('Paste path to HTML file:\n')

try:
    n = int(input('Type table number (1st table as 1):\n'))
except ValueError:
    print('Type table number (1st table as 1, etc.)')

try:
    table = pd.read_html(url)[n - 1]
except NameError:
    print('Type table number (1st table as 1, etc.)')

try:
    table.to_excel(f"{name}.xlsx")
except NameError:
    print('Table is not defined')
    
print('test pr')
