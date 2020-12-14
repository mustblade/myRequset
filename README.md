# myRequset
selenium封装改造V1.0

selenium是个好东西，但是我用起来总觉得很奇怪，感觉作者少封装了一层。

自己小封了一下，详情

import myRequest

#基础信息，_base是selenium对象,start后得到
my = myRequest.myRequest()
url="http://www.baidu.com"
chromedriver = "E:\\chromedriver.exe"
cookie={"key","value"}#吐槽一句，原生的太sb了，这里支持多个字段

#封装启动类start
my.start(url,chromedriver,cookie)

#封装返回类result
print(my.result())

#封装查找类find
print(my.find("wrapper").click())

#封装批量查找类find_list
print(my.find_list("wrapper"))

#封装执行js类exec
my.exec("alert(1)")

