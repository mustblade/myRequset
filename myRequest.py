#encoding=utf-8
from selenium import webdriver
class myRequest:
    def __init__(self):

        #假私有变量
        self._base = None
        self._page=None

        #宏定义
        self.ID=0
        self.NAME=1
        self.CSS=2
        self.XPATH=3

    #开启访问
    def start(self,url,chromedriver,cookie=None,time=1):
        self._base = webdriver.Chrome(executable_path =chromedriver)
        self._base.implicitly_wait(time)
        self._base.get(url)
        if(cookie!=None):
            for i in cookie:
                self._base.add_cookie({"name":i,"value":cookie[i]})
                self._base.get(url)

    #结果查询
    def result(self):
        self._page=self._base.page_source
        return self._page

    def find(self,s,type=0):
        if(type==self.ID):
            location=self._base.find_element_by_id(s)
        if (type == self.NAME):
            location=self._base.find_element_by_name(s)
        if(type==self.CSS):
            location=self._base.find_element_by__css_selector(s)
        if(type==self.XPATH):
            location=self._base.find_element_by_xpath(s)
        return location

    def find_list(self, s, type=0):
        if (type == self.ID):
            location = self._base.find_elements_by_id(s)
        if (type == self.NAME):
            location = self._base.find_elements_by_name(s)
        if (type == self.CSS):
            location = self._base.find_elements_by__css_selector(s)
        if (type == self.XPATH):
            location = self._base.find_elements_by_xpath(s)
        return location

    def exec(self,cmd):
        self._base.execute_script(cmd)
        while(1):
            ins=input("js执行完毕，继续请输入0：")
            print(type(ins))
            if(ins=="0"):
                return

    def __del__(self):
        self._base.close()