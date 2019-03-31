import unittest
import json
from base.method import method,IsContent
from page.kuai8 import  *
from utils.openationExcel import OpenationExcel
class Kuai8(unittest.TestCase):
    def setUp(self):
        self.obj=method()
        self.p=IsContent()
        self.excle=OpenationExcel()

    def isContent(self,r,row):
        # self.statusCode(r=r)
        self.assertTrue(self.p.isContent(row=row,str2=r.text))

    def statusCode(self,r):
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['msg_num'],0)

    # def test_login_001(self):
    #     r=self.obj.get(1)
    #     list1=[]
    #     user_ifo=r.json()['result']
    #     list1.append(user_ifo)
    #     writeuser(json.dumps(list1))
    #     self.isContent(r=r, row=1)

    def test_login_001(self):
        r=self.obj.get(url=getUrl('18810037430'))
        print(r.json())
        self.isContent(r=r,row=1)
        self.excle.writeReuslt(1,'pass')

    def test_login_002(self):
        r=self.obj.get(url=getUrl('188100374301'))
        self.isContent(r=r,row=2)
        print(r.json())
        self.excle.writeReuslt(2,'pass')


    def test_like_001(self):
        data={}
        data['like']=1,
        data['smid']='X14zVGRHoZWDzJiXjw5ezciRKSnCSDFP'
        r=self.obj.post2(row=3,data=data)
        self.isContent(r=r,row=3)
        print(r.json())
        self.excle.writeReuslt(3,'pass')

        # self.isContent(r=3,row=3)
if __name__ == '__main__':
    unittest.main(verbosity=2)