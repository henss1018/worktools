import openpyxl, os
from openpyxl.styles import Font


def mutiplicationTable(in_mitrix):
    os.chdir('D:\\python\\test')
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')
    for i in range(2, int(in_mitrix)+2, 1):
        sheet.cell(row=1, column=i).value = i-1
        sheet.cell(row=i, column=1).value = i-1
    for j in range(2, int(in_mitrix)+2, 1):
        for k in range(2,int(in_mitrix)+2, 1):
            sheet.cell(row=j, column=k).value = int(sheet.cell(row=j, column=1).value
                                                    ) * int(sheet.cell(row=1, column=k).value)
    wb.save('mutiplication_table.xlsx')


mutiplicationTable(100)