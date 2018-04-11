# coding: utf-8 

from jira import JIRA
import time
import requests
import json

#与jira建连
P1 = JIRA('http://qa.nibirutech.com/jira',basic_auth=('hezhengguang','Hzgdhr1234'))

#钉钉机器人webhook接口地址
url = "https://oapi.dingtalk.com/robot/send?access_token=858a351e387c017d89f275e926ef65779cfe27673219e3a1f18d768991313e29"

#请求头
h = {"Content-Type" : "application/json;charset=utf-8"}

#赋值一个变量，使其与检索到的最新bug key做比较
i = 10213

##构建一个无限循环，使最新的bug被发送至钉钉机器人
while True:
    issueslist = P1.search_issues('project = "P1" and created >= "-10d" and status = "待验证"',maxResults=10)
    bugkey = str(issueslist[0])
    bug = int(bugkey[3:])           #取到最新bug的key和具体数字

    issue = P1.issue(bugkey)
    summary = issue.fields.summary  #取到最新bug的summary
    
    man = issue.fields.assignee #取到最新bug的assignee
    
    link = "http://qa.nibirutech.com/jira/browse/" + bugkey #bug链接，通用格式加bugkey即可
    bugmsg = {                  #post内容，格式严格按照钉钉机器人文档
    "msgtype": "link", 
    "link": {
        "text": summary,
        "title": str(man)+"，你的bug已被修复，赶快验证一下！",
        "picUrl":"",
        "messageUrl":link,
         }
      }
    bugmsg = json.dumps(bugmsg)  #将数据转换为json格式，因为钉钉post内容只支持json  
    
    if bug <= i:
        time.sleep(10) #程序挂起10秒（为防止运行过于频繁,造成内存资源占用过度）
        continue

    else:
        r = requests.post(url, data=bugmsg, headers=h) #请求钉钉机器人webhook接口的完整请求
        i = bug
        time.sleep(10) 
        continue 
