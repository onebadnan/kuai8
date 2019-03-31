def main_run(self):
    '''批量执行测试用例'''
    '''先删除历史Excel case执行结果记录'''
    self.remo_excel()
    fp = os.path.join(os.path.abspath(os.path.dirname('../report')), 'report', self.getNowTime() + 'testreport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(fp, 'wb'),
        title='接口自动化测试报告',
        description='自动化测试报告'
    ).run(self.getSuite())
    # unittest.TextTestRunner().run(self.getSuite())
    # content = '通过数:{0}   失败数:{1}   通过率:{2}'.format(
    #     self.excel.run_success_result(),
    #     self.excel.run_fail_result(), self.excel.run_pass_rate())
    print('Please wait while the statistics test results are sent in the mail')
    latest_report_dir = self.latest_report(os.path.join(os.path.abspath(os.path.dirname('../report')), 'report'))

    self.send_mail(['844916536@qq.com', 'lwj.198@163.com'], '接口自动化测试报告', latest_report_dir)


#
if __name__ == "__main__":
    Runner().main_run()