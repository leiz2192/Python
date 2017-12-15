#/usr/bin/python
# -*- coding:utf-8 -*-

import xlwt
import xlrd

def xl_wt():
    work_book = xlwt.Workbook(encoding='ascii')
    work_sheet = work_book.add_sheet("Xl-Exercise")
    work_sheet.write(0, 0, "Hello World")
    work_sheet.write(1, 0, "陕西西安")
    work_book.save("xl-exercise.xls")


def xl_rd():
    work_book = xlrd.open_workbook("xl-exercise.xls")
    work_sheet = work_book.sheet_by_name('Xl-Exercise')
    print("total rows:", work_sheet.nrows)
    print("total cols:", work_sheet.ncols)
    print(work_sheet.cell(0, 0).value)
    print(work_sheet.cell(1, 0).value)

if __name__ == "__main__":
    xl_wt()
    xl_rd()

