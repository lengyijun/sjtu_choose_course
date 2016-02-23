# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
   main_page="http://electsys.sjtu.edu.cn/edu/index.aspx"
   r=requests.session()

   req_get1=r.get(main_page)
   cookie1=req_get1.headers['Set-Cookie']
   post_data={
        'txtUserName':'5140809011',
        'txtPwd':'08050019',
        'rbtnLst':'1',
        'Button1':'登录',
   }
   header1={
       'Connection':'keep-alive',
       'Cache-Control':'max-age=0',
       'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Origin':'http://electsys.sjtu.edu.cn',
       'Upgrade-Insecure-Requests':1,
       'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
       #'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
       'Content-Type':'application/x-www-form-urlencoded',
       'Referer':'http://electsys.sjtu.edu.cn/edu/index.aspx',
       'Accept-Encoding':'gzip, deflate',
       'Accept-Language':'zh-CN,zh;q=0.8',
       'Cookie':cookie1
   }

   soup=BeautifulSoup(req_get1.content)
   post_data['__VIEWSTATEGENERATOR']=soup.find("input",{"name":"__VIEWSTATEGENERATOR"}).get("value")
   post_data['__VIEWSTATE']=soup.find("input",{"name":"__VIEWSTATE"}).get("value")
   post_data['__EVENTVALIDATION']=soup.find("input",{"name":"__EVENTVALIDATION"}).get("value")

   req_post1=r.post(main_page,data=post_data,headers=header1)

   url_third="http://electsys.sjtu.edu.cn/edu/student/elect/electwarning.aspx?xklc=3"
   post_data={}
   soup=BeautifulSoup(r.get(url_third).content)
   post_data['__VIEWSTATEGENERATOR']=soup.find("input",{"name":"__VIEWSTATEGENERATOR"}).get("value")
   post_data['__VIEWSTATE']=soup.find("input",{"name":"__VIEWSTATE"}).get("value")
   post_data['__EVENTVALIDATION']=soup.find("input",{"name":"__EVENTVALIDATION"}).get("value")
   post_data['CheckBox1']="on"
   post_data['btnContinue']="继续"

   req_post2=r.post("http://electsys.sjtu.edu.cn/edu/student/elect/electwarning.aspx?xklc=3",
                    data=post_data)
#    以上登录到选课主页,接下去是去任选课一栏

   post_data={}
   soup=BeautifulSoup(req_post2.content)
   post_data['__EVENTVALIDATION']=soup.find("input",{"name":"__EVENTVALIDATION"}).get("value")
   post_data['__VIEWSTATEGENERATOR']=soup.find("input",{"name":"__VIEWSTATEGENERATOR"}).get("value")
   post_data['__VIEWSTATE']=soup.find("input",{"name":"__VIEWSTATE"}).get("value")
   post_data['SpeltyRequiredCourse1$btnXuanXk']="任选课"

   header1['Referer']="http://electsys.sjtu.edu.cn/edu/student/elect/speltyRequiredCourse.aspx"
   req_post3=r.post('http://electsys.sjtu.edu.cn/edu/student/elect/speltyRequiredCourse.aspx',
        data=post_data,headers=header1)
   req_get2=r.get("http://electsys.sjtu.edu.cn/edu/student/elect/outSpeltyEP.aspx")

   post_data={}
   soup=BeautifulSoup(req_get2.content)
   post_data['__VIEWSTATE']=soup.find("input",{"name":"__VIEWSTATE"}).get("value")
   post_data['__VIEWSTATEGENERATOR']=soup.find("input",{"name":"__VIEWSTATEGENERATOR"}).get("value")
   post_data['__EVENTVALIDATION']=soup.find("input",{"name":"__EVENTVALIDATION"}).get("value")
   post_data['OutSpeltyEP1$dpYx']="03000"
   post_data['OutSpeltyEP1$dpNj']="2013"
   post_data['OutSpeltyEP1$btnQuery']="查 询"

   header1['Referer']="http://electsys.sjtu.edu.cn/edu/student/elect/outSpeltyEP.aspx"
   header1["Upgrade-Insecure-Requests"]="1"
   req_post4=r.post("http://electsys.sjtu.edu.cn/edu/student/elect/outSpeltyEP.aspx",
        data=post_data,headers=header1)

#    以上得到2013级电院的课
   post_data={}
   soup=BeautifulSoup(req_post4.content)
   post_data['__VIEWSTATE']=soup.find("input",{"name":"__VIEWSTATE"}).get("value")
   post_data['__VIEWSTATEGENERATOR']=soup.find("input",{"name":"__VIEWSTATEGENERATOR"}).get("value")
   post_data['__EVENTVALIDATION']=soup.find("input",{"name":"__EVENTVALIDATION"}).get("value")
   post_data['OutSpeltyEP1$dpYx']="03000"
   post_data['OutSpeltyEP1$dpNj']="2013"
   post_data['myradiogroup']="cs353"
   post_data['OutSpeltyEP1$lessonArrange']="课程安排"
   req_post4=r.post("http://electsys.sjtu.edu.cn/edu/student/elect/outSpeltyEP.aspx",data=post_data,
                    headers=header1)
   print(req_post4.content)

   post_data={}
   soup=BeautifulSoup(req_post4.content)
   post_data['__VIEWSTATE']=soup.find("input",{"name":"__VIEWSTATE"}).get("value")
   post_data['__VIEWSTATEGENERATOR']=soup.find("input",{"name":"__VIEWSTATEGENERATOR"}).get("value")
   post_data['__EVENTVALIDATION']=soup.find("input",{"name":"__EVENTVALIDATION"}).get("value")
   post_data['myradiogroup']=soup.find("input",{"name":"myradiogroup"}).get("value")
   post_data['LessonTime1$btnChoose']="选定此教师"

   header1['Referer']="http://electsys.sjtu.edu.cn/edu/lesson/viewLessonArrange.aspx?kcdm=cs353&xklx=%e9%80%89%e4%bf%ae&redirectForm=outSpeltyEp.aspx&yxdm=03000&nj=2013&kcmk=-1&txkmk=-1"
   req_post4=r.post("http://electsys.sjtu.edu.cn/edu/lesson/viewLessonArrange.aspx?kcdm=cs353&xklx=%u9009%u4fee&redirectForm=outSpeltyEp.aspx&yxdm=03000&nj=2013&kcmk=-1&txkmk=-1",
                    data=post_data,headers=header1)
   print(req_post4.content)
