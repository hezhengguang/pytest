# coding: utf-8 

from jira import JIRA
import requests
import json

P1 = JIRA('http://qa.nibirutech.com/jira',basic_auth=('hezhengguang','Hzgdhr1234'))

def url_filter(self):
    url = "http://qa.nibirutech.com/jira/issues/?filter=-4&jql=project%20%3D%20%22P1%22%20and%20created%20%3E%3D%20%22-20d%22%20and%20status%20%3D%20%22待验证%22%20and%20reporter%20%3D%20"+self
    return url

def verified_bug(self):
    content = 'issuetype = Bug and project = "P1" and created >= "-20d" and status = "待验证" and reporter = %s' %self
    issuelist = P1.search_issues(content)
    return issuelist
    
members = ["罗丽","白仕豪","lengzaibin","李映荷","贺正光","应丽梅","周仁德","谢罗霄","刘光鲤","肖培资"]


#钉钉机器人webhook接口地址
url = "https://oapi.dingtalk.com/robot/send?access_token=9b5da23dc35924b724999a33fe617e70003d7434e128ffeba6331b89e21a9bbe"

#请求头
h = {"Content-Type" : "application/json;charset=utf-8"}

for man in members:
    urls = url_filter(man)
    nums = len(verified_bug(man))   
    if nums != 0:
        msg ={
        "msgtype": "link",
        "link":{
        "text": "截止此时，你待验证的bug仍有"+str(nums)+"个哦，加油！",
        "title":str(man)+",请查看你的待验证bug哦",
        "messageUrl":urls,
                 }
        }
        msg = json.dumps(msg)
        r = requests.post(url, data=msg, headers=h)      

    else:
        continue
