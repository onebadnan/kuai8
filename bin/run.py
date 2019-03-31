import unittest
from utils.openationExcel import OpenationExcel
import smtplib
from email.mime.text import MIMEText
import HTMLTestRunner2
import time
import os
from email.header import Header

from email.mime.multipart import MIMEMultipart



class Runner:
    def __init__(self):
        self.excel = OpenationExcel()

    def latest_report(self, report_dir):
        lists = os.listdir(report_dir)
        # 按时间顺序对该目录文件夹下面的文件进行排序
        lists.sort(key=lambda fn: os.path.getatime(report_dir + "/" + fn))
        print("The latest report is:" + lists[-1])

        file = os.path.join(report_dir, lists[-1])
        print(file)
        return file

    def getNowTime(self):
        return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))

    def getSuite(self):
        suite = unittest.TestLoader().discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests'),
			pattern='test_*.py',
			top_level_dir=None)
        return suite


    def send_mail(self,report_dir):
        '''
        发送邮件内容
		:param to_user:发送邮件的人
		:param sub:主题
		:param content:邮件内容
        '''
        smtpserver = 'smtp.qq.com'           #发件服务器
        port=465
        send_user = '316835981@qq.com'      #发送端
        to_user='13439875784@163.com'       #接收端
        # =========编辑邮件内容=========
        f = open(report_dir, 'rb')
        mail_body = f.read()
        f.close()
        msg=MIMEMultipart()
        msg['Subject'] = '接口自动化测试报告'            #主题
        msg['From'] = send_user         #发件人
        msg['To'] = to_user             #收件人
        text = MIMEText(mail_body, 'html', 'utf-8')
        text['Subject'] = Header('接口自动化自动化测试报告', 'utf-8') #定义文件正文标题
        msg.attach(text)
        #-------附件------------
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att.add_header('Content-Disposition', 'attachment', filename='接口自动化测试报告.html')# 定义附件名称
        msg.attach(att)  # 挂起
        server = smtplib.SMTP_SSL(smtpserver,port)
        server.login(send_user,'zbfbslvwmlprbjhb')
        server.sendmail(send_user, to_user,msg.as_string())
        server.close()

    def main_run(self):
        test_report=os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'report')
        filename= os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
                         'report',self.getNowTime() +'testreport.html')
        HTMLTestRunner2.HTMLTestRunner(
            stream=open(filename, 'wb'),
            title='接口自动化测试报告',
            description='自动化测试报告'
        ).run(self.getSuite())
        '''批量执行测试用例'''
        unittest.TextTestRunner().run(self.getSuite())
        # content = '通过数：{0} 失败数：{1} 通过率：{2}'.format(
        #     self.excel.run_success_result(),
        #     self.excel.run_fail_result(), self.excel.run_pass_rate())
        print('Please wait while the statistics test results are sent in the mail')
        latest_report_dir =self.latest_report(test_report)
        self.send_mail(latest_report_dir)
if __name__ == '__main__':
    Runner().main_run()
    # latest_report_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'report')
    # runner=Runner()
    # r=type(runner.latest_report(latest_report_dir))
    # print(r)