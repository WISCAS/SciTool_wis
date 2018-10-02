#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
GUI for ScientificTools
py36 PyQt5

This GUI include a terminal ,forum and browser

author: WIS in IMECAS
last edited: 10/1/2018
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QGridLayout, QTextBrowser,QLineEdit

import webbrowser, sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from doi_get import article_search

class Ui_MainWindow(QWidget):
    item_name = "SciTools V1.2"


    html_url = """
    <!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <script type="text/javascript" src="qwebchannel.js"></script>
    <title>QWebChannel测试</title>
    <script>
        window.onload = function () {
            new QWebChannel(qt.webChannelTransport, function (channel) {
                window.pyjs = channel.objects.pyjs;
                pyjs.myHello(alert);
            });
        }
    </script>
</head>
<body>
<div id="test">
    this is test !
</div>
<div onclick="qt5test();">测试</div>

<script>
    function qt5test() {
       pyjs.myTest('这是测试传参的',function (res) {
            alert(res);
        });
    }
    function uptext(msg) {
        document.getElementById('test').innerHTML=msg;
    }
</script>
</body>
</html>
    
    """
    def __init__(self):
        super().__init__()
        self.initUI()
        self.Key_Dict = {'q':''}

    def initUI(self):
        # self.tips_1 = QLabel("网站：<a href='http://code.py40.com'>http://code.py40.com</a>");
        # self.tips_1.setOpenExternalLinks(True)

        self.titlebox = QLineEdit(self)
        self.title = QLabel("Title:")
        self.webView = QTextBrowser()
        self.webView.setText("这是搜索结果显示框")
        self.webView.setOpenExternalLinks(True)
        self.statusView = QTextBrowser()
        self.statusView.setText("这是状态显示框")
        self.btn_webbrowser = QPushButton('search', self)

        self.btn_webbrowser.clicked.connect(self.btn_webbrowser_Clicked)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.title, 2, 0, 1, 1)
        grid.addWidget(self.titlebox, 2, 1, 1, 4)
        grid.addWidget(self.btn_webbrowser, 3, 4, 2, 1)
        grid.addWidget(self.statusView, 10, 0, 5, 5)
        grid.addWidget(self.webView, 0, 5, 15, 10)


        self.setLayout(grid)

        self.resize(1200, 800)
        self.setMinimumSize(0, 0);
        self.setMaximumSize(1200,800);
        self.center()
        self.setWindowTitle(self.item_name)
        self.setWindowIcon(QIcon("icon/scientificTool.png"))
        self.show()

    def btn_webbrowser_Clicked(self):
        self.webView.setText("")
        self.statusView.append("Searching...")
        self.Key_Dict['q'] = self.titlebox.text()
        article_search(self, self.Key_Dict)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def web_append(self, text):
        self.webView.append(text)

    def status_append(self, text):
        self.statusView.append(text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Ui_MainWindow()
    sys.exit(app.exec_())
