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


url = "https://www.1mg.com/drugs/dolo-650-tablet-74467"
r = Render(url)
soup = BeautifulSoup(r.frame.toHtml(),features="lxml")
value = soup.find_all("div",{"class":"saltInfo"})
#print(value)
for values in value:
    for link in BeautifulSoup(str(values),"html.parser").find("a").text:
        #if 'href' in link.attrs:
        print(link)