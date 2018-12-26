# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'Hari')
sheet1.write(2, 0, 'Chandra')
sheet1.write(3, 0, 'Prasad')

sheet1.write(0, 1, 'Python')
sheet1.write(0, 2, 'Tutorial')
sheet1.write(0,3, 'Learning')


wb.save('xlwt example.xls')
