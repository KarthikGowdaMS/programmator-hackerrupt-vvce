'''
Program to web scrap from a tag, get it's link and go to another page which in turn provides 
another value from that page which is scrapped.
'''

#Modules to be imported 
import sys
import requests
import html5lib
import lxml #pip3 install lxml
from bs4 import BeautifulSoup
from PyQt5.QtGui import * #pip3 install PyQt5
from PyQt5.QtCore import * #pip3 install PyQt5
from PyQt5.QtWebKit import * #pip3 install PyQt5
from PyQt5.QtWebKitWidgets import QWebPage #pip3 install PyQt5
from PyQt5.QtWidgets import * #pip3 install PyQt5
#Modules end here

class Render(QWebPage):
    def _init_(self,url):
        self.app=QApplication(sys.argv)
        QWebPage._init_(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self,result):
        self.frame = self.mainFrame()
        self.app.quit()


Website_URL = "https://www.1mg.com/search/all?filter=true&name=Dolo%20650"
r = Render(Website_URL)
soup = BeautifulSoup(r.frame.toHtml(),features="lxml")
table = soup.find_all("div",{"class":"col-xs-12"})
for names in table:
    for link in BeautifulSoup(str(names),"html.parser").findAll("a"):
        if 'href' in link.attrs:
            drug = "htps://www.1mg.com"+link['href']
            print(drug)