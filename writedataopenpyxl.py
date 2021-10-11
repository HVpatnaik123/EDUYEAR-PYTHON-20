import openpyxl

path = 'C:/Users/user/Desktop/xyz.xlsx'
workbook = openpyxl.load_workbook(path)

sheet = workbook.get_sheet_by_name('hello')

for r in range(1,5):
    for c in range (1,3):
        input_var = input('enter text: ')
        sheet.cell(row=r, column=c).value = input_var
workbook.save(path)