import xlrd
import os
from framework.logger import Logger

logger=Logger("logger=Util").getlog()

class Util(object):

    @classmethod
    def read_excel(self,excelPath,sheetName="Sheet1"):

        workBook = xlrd.open_workbook(excelPath)
        sheet = workBook.sheet_by_name(sheetName)
        keys = sheet.row_values(0)
        rowNum = sheet.nrows
        cowNum = sheet.ncols
        
        if rowNum <= 1:
            logger.error("excel表中数据小于1")
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data = { }
                values=sheet.row_values(i)
                for j in range(cowNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
            return r

if __name__=="__main__":

    print(Util.read_excel("C:/Users/Administrator/PycharmProjects/search/excel.xlsx","Sheet1"))