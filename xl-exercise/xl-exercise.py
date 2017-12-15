#/usr/bin/python
# -*- coding:utf-8 -*-

import xlwt
import xlrd
from xlutils.copy import copy

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


def xl_append():
    rd_book = xlrd.open_workbook("xl-exercise.xls")
    wt_book = copy(rd_book)
    wt_sheet = wt_book.get_sheet(0)
    wt_sheet.write(0, 1, "new world")
    wt_book.save("xl-exercise.xls")


if __name__ == "__main__":
    xl_wt()
    xl_rd()
    xl_append()

