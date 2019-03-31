import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excle_data import *


def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


class OpenationExcel:
    def get_excle(self):
        db = xlrd.open_workbook(data_dir('data', 'api.xls'))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取行数'''
        return self.get_excle().nrows

    def get_row_cel(self, row, col):
        '''获取单元格内容'''
        return self.get_excle().cell_value(row, col)

    def get_url(self, row):
        '''获取测试ID'''
        return self.get_row_cel(row, getCaseID())

    def get_url(self, row):
        '''获取请求地址'''
        return self.get_row_cel(row, get_url())

    def get_request_data(self, row):
        '''获取请求参数'''
        return self.get_row_cel(row, get_request_data())

    def get_expect(self, row):
        '''获取期望结果'''
        return self.get_row_cel(row, get_expect())

    def get_result(self, row):
        '''获取实际结果'''
        return self.get_row_cel(row, get_result())

    def writeReuslt(self, row, content):
        '''把测试结果写入文件中'''
        col = get_result()
        work = xlrd.open_workbook(data_dir('data', 'api.xls'))
        print(work)
        old_comment = copy(work)
        ws = old_comment.get_sheet(0)
        ws.write(row, col, content)
        old_comment.save(data_dir('data', 'api.xls'))


    def run_success_result(self):
        '''获取所有成功测试用例数量'''
        pass_count=[]
        fail_count=None
        for i in range(1,self.get_rows()):
            if self.get_result(i)=='pass':
                pass_count.append(i)
        return int(len(pass_count))

    def run_fail_result(self):
        return int((self.get_rows()-1)-self.run_success_result())

    def run_pass_rate(self):
        '''成功数除以总数'''
        rate=''
        if self.run_fail_result()==0:
            rate='100%'
        elif self.run_fail_result()!=0:
            rate=str(int(self.run_success_result()/int(self.get_rows()-1)*100))+'%'
        return rate

if __name__ == '__main__':
    opea = OpenationExcel()
    print(base_dir('api.xls'))
