# pytestmaster
programming practices

The script final.py is writed on Python3, and only support running on Python3.
It is only used in P1 group, thanks!

4.6
完成v1.0版jira-钉钉推送脚本。但在测试过程中发现：jira认证接口有请求次数显示，在挂了一中午之后开始报错。得出：使用自定义函数不方便进行循环。

4.8
更新V1.1，去掉自定义函数，只在开头jira建立一次连接，将完整请求直接写在循环中。避免出现认证次数超上限的情况。风险：不知道jira一次建连后能坚持多久
