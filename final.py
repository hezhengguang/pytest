# coding: utf-8 

from jira import JIRA
import time
import requests
import json

#定义一个函数，使其检索出最新的bug，并将bug key的数字返回
def issue_search():
    P1 = JIRA('http://qa.nibirutech.com/jira',basic_auth=('hezhengguang','Hzgdhr1234'))
    issueslist = P1.search_issues('project = "P1" and created >= "-10d"',maxResults=10)
    bugbug = str(issueslist[0])
    bug = bugbug[3:]
    return bug

#定义一个函数，可以检索出输入的bug key对应的summary
def issue_summary(self):
    P1 = JIRA('http://qa.nibirutech.com/jira',basic_auth=('hezhengguang','Hzgdhr1234'))
    issue = P1.issue(self)
    summary = issue.fields.summary
    return summary

#定义一个函数，检索出bug key对应的责任人
def issue_assignee(self):
    P1 = JIRA('http://qa.nibirutech.com/jira',basic_auth=('hezhengguang','Hzgdhr1234'))
    issue = P1.issue(self)
    assignee = issue.fields.assignee
    return assignee

#钉钉机器人webhook接口地址
url = "https://oapi.dingtalk.com/robot/send?access_token=858a351e387c017d89f275e926ef65779cfe27673219e3a1f18d768991313e29"

#请求头
h = {"Content-Type" : "application/json;charset=utf-8"}

#赋值一个变量，使其与检索到的最新bug key做比较
i = int(issue_search())

##构建一个无限循环，使最新的bug被发送至钉钉机器人
while True:
    bug = issue_search()
    summary = issue_summary('P1-'+bug)
    man = issue_assignee('P1-'+bug)
    link = "http://qa.nibirutech.com/jira/browse/" + str('P1-'+bug) #bug链接，通用格式加bugkey即可
    bugmsg = {                  #post内容，格式严格按照钉钉机器人文档
    "msgtype": "link", 
    "link": {
        "text": summary,
        "title": "又来了个bug, "+str(man)+"快看!",
        "picUrl":"",
        "messageUrl":link,
         }
      }
    bugmsg = json.dumps(bugmsg)
    
    if int(bug) == i:
        time.sleep(10) #程序挂起10秒（为防止运行过于频繁,造成内存资源占用过度）
        continue

    else:
        r = requests.post(url, data=bugmsg, headers=h) #请求钉钉机器人webhook接口的完整请求
        i = i+1
        time.sleep(10) 
        continue    


