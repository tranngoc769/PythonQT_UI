# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import asyncio
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt5.QtGui import QIcon
from telethon import TelegramClient, client
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import JoinChannelRequest,LeaveChannelRequest


def ReadAccountList():
        list_accs = []
        with open('accounts.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                        if line_count == 0:
                                line_count += 1
                        else:
                                list_accs.append([row[0],row[1],row[2]])
                                line_count += 1
        return list_accs
class Ui_MainWindow(object):
        async def change_name_auto(self,name, phone):
                try_again = 0
                while try_again < 5:
                        try_again += 1
                        try:
                                str_log = phone[0:5] + "xxxxxx"
                                self.addLog("Change account phone " + str_log + " --> "+ name)
                                await self.tele_client(UpdateProfileRequest(last_name="", first_name=name, about =name))
                                return;
                        except KeyboardInterrupt:
                                # await self.tele_client.start()
                                await self.tele_client(UpdateProfileRequest(last_name=''))
                                sys.exit()
                        except Exception as e:
                                print('%s: %s' % (type(e), e))
                        await asyncio.sleep(1)
        async def change_name_main(self,loop,name, phone):
                await self.tele_client.start()
                task = loop.create_task(self.change_name_auto( name, phone))
                await task
                await self.tele_client.disconnect()
                task.cancel()
        async def join_leave_channel(self, url,phone, mode):
                try:
                        str_log = phone[0:5] + "xxxxxx"
                        if mode == 1:
                                await self.tele_client(JoinChannelRequest(url))
                                self.addLog("Phone " + str_log + " joined "+ url)
                        else:
                                await self.tele_client(LeaveChannelRequest(url))
                                self.addLog("Phone " + str_log + " leave "+ url)
                except Exception as err:
                        print(err)
        async def join_leave_channel_main(self,loop,url, phone, mode):
                await self.tele_client.start()
                task = loop.create_task(self.join_leave_channel( url, phone, mode))
                await task
                await self.tele_client.disconnect()
                task.cancel()
        def setupUi(self, MainWindow):
                self.isRun = False
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1365, 810)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1402, 802))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.ContentTab = QtWidgets.QTabWidget(self.verticalLayoutWidget)
                self.ContentTab.setMinimumSize(QtCore.QSize(1400, 800))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.ContentTab.setFont(font)
                self.ContentTab.setTabPosition(QtWidgets.QTabWidget.North)
                self.ContentTab.setTabShape(QtWidgets.QTabWidget.Rounded)
                self.ContentTab.setIconSize(QtCore.QSize(25, 25))
                self.ContentTab.setElideMode(QtCore.Qt.ElideMiddle)
                self.ContentTab.setTabsClosable(False)
                self.ContentTab.setMovable(False)
                self.ContentTab.setTabBarAutoHide(True)
                self.ContentTab.setObjectName("ContentTab")
                self.Workplace = QtWidgets.QWidget()
                self.Workplace.setObjectName("Workplace")
                self.horizontalLayoutWidget = QtWidgets.QWidget(self.Workplace)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(2, 9, 1361, 731))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.MainFrame = QtWidgets.QFrame(self.horizontalLayoutWidget)
                self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.MainFrame.setObjectName("MainFrame")
                self.ListUserGroup = QtWidgets.QGroupBox(self.MainFrame)
                self.ListUserGroup.setGeometry(QtCore.QRect(20, 420, 641, 291))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(False)
                font.setWeight(50)
                self.ListUserGroup.setFont(font)
                self.ListUserGroup.setStyleSheet("")
                self.ListUserGroup.setObjectName("ListUserGroup")
                self.ListUserFrame = QtWidgets.QFrame(self.ListUserGroup)
                self.ListUserFrame.setGeometry(QtCore.QRect(9, 19, 631, 311))
                self.ListUserFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.ListUserFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.ListUserFrame.setObjectName("ListUserFrame")
                self.ListUserScroll = QtWidgets.QScrollArea(self.ListUserFrame)
                self.ListUserScroll.setGeometry(QtCore.QRect(9, 9, 611, 251))
                self.ListUserScroll.setStyleSheet("QScrollArea{background :rgb(255, 255, 255)}")
                self.ListUserScroll.setWidgetResizable(True)
                self.ListUserScroll.setObjectName("ListUserScroll")
                self.ListUserScrollContent = QtWidgets.QWidget()
                self.ListUserScrollContent.setGeometry(QtCore.QRect(0, 0, 609, 249))
                self.ListUserScrollContent.setAutoFillBackground(True)
                self.ListUserScrollContent.setObjectName("ListUserScrollContent")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ListUserScrollContent)
                self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
                self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
               
                self.ListUserScroll.setWidget(self.ListUserScrollContent)
                self.JoinLeaveGroup = QtWidgets.QGroupBox(self.MainFrame)
                self.JoinLeaveGroup.setGeometry(QtCore.QRect(20, 220, 641, 181))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(False)
                font.setWeight(50)
                self.JoinLeaveGroup.setFont(font)
                self.JoinLeaveGroup.setStyleSheet("")
                self.JoinLeaveGroup.setAlignment(QtCore.Qt.AlignCenter)
                self.JoinLeaveGroup.setObjectName("JoinLeaveGroup")
                self.URLGroup = QtWidgets.QGroupBox(self.JoinLeaveGroup)
                self.URLGroup.setGeometry(QtCore.QRect(19, 39, 481, 71))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.URLGroup.setFont(font)
                self.URLGroup.setObjectName("URLGroup")
                self.InputURL = QtWidgets.QLineEdit(self.URLGroup)
                self.InputURL.setGeometry(QtCore.QRect(12, 25, 461, 31))
                self.InputURL.setStyleSheet("QLineEdit{border: 1px solid rgb(173, 173, 173);    border-radius: 5px;    background:transparent;    padding :  0px 10px;}")
                self.InputURL.setObjectName("InputURL")
                self.TimeJLGroup = QtWidgets.QGroupBox(self.JoinLeaveGroup)
                self.TimeJLGroup.setGeometry(QtCore.QRect(510, 39, 111, 71))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.TimeJLGroup.setFont(font)
                self.TimeJLGroup.setObjectName("TimeJLGroup")
                self.InputTimeJL = QtWidgets.QSpinBox(self.TimeJLGroup)
                self.InputTimeJL.setGeometry(QtCore.QRect(10, 25, 81, 31))
                self.InputTimeJL.setStyleSheet("QSpinBox{    border: 1px solid rgb(173, 173, 173);border-radius: 5px;    background:transparent;}")
                self.InputTimeJL.setAlignment(QtCore.Qt.AlignCenter)
                self.InputTimeJL.setObjectName("InputTimeJL")
                self.InputTimeJL.setValue(1)
                self.JoinGroupBtn = QtWidgets.QPushButton(self.JoinLeaveGroup)
                self.JoinGroupBtn.setGeometry(QtCore.QRect(20, 120, 231, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.JoinGroupBtn.setFont(font)
                self.JoinGroupBtn.setStyleSheet("QPushButton{background: rgb(225, 225, 225);border-radius: 10px;color:black;}")
                self.JoinGroupBtn.setObjectName("JoinGroupBtn")
                self.LeaveGroupBtn = QtWidgets.QPushButton(self.JoinLeaveGroup)
                self.LeaveGroupBtn.setGeometry(QtCore.QRect(270, 120, 231, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.LeaveGroupBtn.setFont(font)
                self.LeaveGroupBtn.setStyleSheet("QPushButton{background: rgb(225, 225, 225);border-radius: 10px;color:black;}")
                self.LeaveGroupBtn.setObjectName("LeaveGroupBtn")
                self.JLProcess = QtWidgets.QPushButton(self.JoinLeaveGroup)
                self.JLProcess.setGeometry(QtCore.QRect(514, 125, 101, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.JLProcess.setFont(font)
                self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(252, 234, 160);}")
                self.JLProcess.setObjectName("JLProcess")
                self.ChangeNameGroup = QtWidgets.QGroupBox(self.MainFrame)
                self.ChangeNameGroup.setGeometry(QtCore.QRect(20, 10, 641, 171))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(False)
                font.setWeight(50)
                self.ChangeNameGroup.setFont(font)
                self.ChangeNameGroup.setStyleSheet("")
                self.ChangeNameGroup.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                self.ChangeNameGroup.setObjectName("ChangeNameGroup")
                self.NameGroup = QtWidgets.QGroupBox(self.ChangeNameGroup)
                self.NameGroup.setGeometry(QtCore.QRect(20, 30, 481, 71))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.NameGroup.setFont(font)
                self.NameGroup.setStyleSheet("")
                self.NameGroup.setObjectName("NameGroup")
                self.InputName = QtWidgets.QLineEdit(self.NameGroup)
                self.InputName.setGeometry(QtCore.QRect(12, 25, 461, 31))
                self.InputName.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.InputName.setStyleSheet("QLineEdit{border: 1px solid rgb(173, 173, 173);    border-radius: 5px;    background:transparent;    padding :  0px 10px;}")
                self.InputName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.InputName.setObjectName("InputName")
                self.TimeNameGroup = QtWidgets.QGroupBox(self.ChangeNameGroup)
                self.TimeNameGroup.setGeometry(QtCore.QRect(510, 30, 111, 71))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                self.TimeNameGroup.setFont(font)
                self.TimeNameGroup.setObjectName("TimeNameGroup")
                self.InputTimeName = QtWidgets.QSpinBox(self.TimeNameGroup)
                self.InputTimeName.setGeometry(QtCore.QRect(10, 25, 81, 31))
                self.InputTimeName.setStyleSheet("QSpinBox{    border: 1px solid rgb(173, 173, 173);border-radius: 5px;    background:transparent;}")
                self.InputTimeName.setAlignment(QtCore.Qt.AlignCenter)
                self.InputTimeName.setObjectName("InputTimeName")
                self.ChangeNameBtn = QtWidgets.QPushButton(self.ChangeNameGroup)
                self.ChangeNameBtn.setGeometry(QtCore.QRect(20, 110, 481, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.ChangeNameBtn.setFont(font)
                self.ChangeNameBtn.setStyleSheet("QPushButton{background: rgb(225, 225, 225);border-radius: 10px;color:black;}")
                self.ChangeNameBtn.setObjectName("ChangeNameBtn")
                self.NameProcess = QtWidgets.QPushButton(self.ChangeNameGroup)
                self.NameProcess.setGeometry(QtCore.QRect(514, 115, 101, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.NameProcess.setFont(font)
                self.NameProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(252, 234, 160);}")
                self.NameProcess.setObjectName("NameProcess")
                self.horizontalLayout.addWidget(self.MainFrame)
                self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
                self.line.setFrameShape(QtWidgets.QFrame.VLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.horizontalLayout.addWidget(self.line)
                self.LogFrame = QtWidgets.QFrame(self.horizontalLayoutWidget)
                self.LogFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.LogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.LogFrame.setObjectName("LogFrame")
                self.LogGroup = QtWidgets.QGroupBox(self.LogFrame)
                self.LogGroup.setGeometry(QtCore.QRect(10, 20, 651, 691))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(False)
                font.setWeight(50)
                self.LogGroup.setFont(font)
                self.LogGroup.setAlignment(QtCore.Qt.AlignCenter)
                self.LogGroup.setObjectName("LogGroup")
                self.LogScrollFrame = QtWidgets.QFrame(self.LogGroup)
                self.LogScrollFrame.setGeometry(QtCore.QRect(-1, 19, 651, 671))
                self.LogScrollFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.LogScrollFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.LogScrollFrame.setObjectName("LogScrollFrame")
                self.LogScrollContent = QtWidgets.QScrollArea(self.LogScrollFrame)
                self.LogScrollContent.setGeometry(QtCore.QRect(9, 9, 631, 651))
                self.LogScrollContent.setWidgetResizable(True)
                self.LogScrollContent.setObjectName("LogScrollContent")
                self.LogScrollContentBlog = QtWidgets.QWidget()
                self.LogScrollContentBlog.setGeometry(QtCore.QRect(0, 0, 629, 649))
                self.LogScrollContentBlog.setAutoFillBackground(True)
                self.LogScrollContentBlog.setObjectName("LogScrollContentBlog")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.LogScrollContentBlog)
                self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
                self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
                self.verticalLayout_3.setObjectName("verticalLayout_3")

                self.LogScrollContent.setWidget(self.LogScrollContentBlog)
                self.horizontalLayout.addWidget(self.LogFrame)
                self.ContentTab.addTab(self.Workplace, "")
                self.User = QtWidgets.QWidget()
                self.User.setObjectName("User")
                self.ContentTab.addTab(self.User, "")
                self.verticalLayout.addWidget(self.ContentTab)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1365, 21))
                self.menubar.setObjectName("menubar")
                self.menuFile = QtWidgets.QMenu(self.menubar)
                self.menuFile.setObjectName("menuFile")
                self.menuAbout = QtWidgets.QMenu(self.menubar)
                self.menuAbout.setObjectName("menuAbout")
                self.menuExit = QtWidgets.QMenu(self.menubar)
                self.menuExit.setObjectName("menuExit")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.actionOpen = QtWidgets.QAction(MainWindow)
                self.actionOpen.setObjectName("actionOpen")
                self.actionSave = QtWidgets.QAction(MainWindow)
                self.actionSave.setObjectName("actionSave")
                self.actionExit = QtWidgets.QAction(MainWindow)
                self.actionExit.setObjectName("actionExit")
                self.menuFile.addSeparator()
                self.menuFile.addAction(self.actionOpen)
                self.menuFile.addAction(self.actionSave)
                self.menuFile.addAction(self.actionExit)
                self.menubar.addAction(self.menuFile.menuAction())
                self.menubar.addAction(self.menuAbout.menuAction())
                self.menubar.addAction(self.menuExit.menuAction())

                self.retranslateUi(MainWindow)
                self.ContentTab.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
                MainWindow.setWindowTitle(_translate("MainWindow", "Telegram Multi Program Ver1.0"))
                self.ListUserGroup.setTitle(_translate("MainWindow", "List User"))
                self.JoinLeaveGroup.setTitle(_translate("MainWindow", "Group / Channel Auto Join - Leave"))
                self.URLGroup.setTitle(_translate("MainWindow", "Group / Change URL"))
                self.InputURL.setPlaceholderText(_translate("MainWindow", "https://t.me/<name>"))
                self.TimeJLGroup.setTitle(_translate("MainWindow", "Time Delay"))
                self.JoinGroupBtn.setText(_translate("MainWindow", "Start Join Group"))
                self.LeaveGroupBtn.setText(_translate("MainWindow", "Start Leave Group"))
                self.JLProcess.setText(_translate("MainWindow", "STOP"))
                self.ChangeNameGroup.setTitle(_translate("MainWindow", "Auto Change Telegram Name"))
                self.NameGroup.setTitle(_translate("MainWindow", "Name to change"))
                self.InputName.setPlaceholderText(_translate("MainWindow", "Input name to change"))
                self.TimeNameGroup.setTitle(_translate("MainWindow", "Time Delay"))
                self.ChangeNameBtn.setText(_translate("MainWindow", "Start Change Name"))
                self.NameProcess.setText(_translate("MainWindow", "STOP"))
                self.LogGroup.setTitle(_translate("MainWindow", "LOG"))
                self.ContentTab.setTabText(self.ContentTab.indexOf(self.Workplace), _translate("MainWindow", "Workplace"))
                self.ContentTab.setTabText(self.ContentTab.indexOf(self.User), _translate("MainWindow", "User"))
                self.menuFile.setTitle(_translate("MainWindow", "File"))
                self.menuAbout.setTitle(_translate("MainWindow", "About"))
                self.menuExit.setTitle(_translate("MainWindow", "Exit"))
                self.actionOpen.setText(_translate("MainWindow", "Open"))
                self.actionSave.setText(_translate("MainWindow", "Save"))
                self.actionExit.setText(_translate("MainWindow", "Exit"))
        def setevent(self, MainWindow):
                self.ChangeNameBtn.clicked.connect(self.ChangeNameFunc)
                self.JoinGroupBtn.clicked.connect(self.JoinGroupFunc)
                self.LeaveGroupBtn.clicked.connect(self.LeaveGroupFunc)
                pass
        def  ChangeNameFunc(self):
                if self.isRun == False:
                        self.isRun = True
                        _translate = QtCore.QCoreApplication.translate
                        self.NameProcess.setText(_translate("MainWindow", "STOP"))
                        self.NameProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(252, 234, 160);}")
                        QtWidgets.QApplication.processEvents()
                        # RUNING
                        self.NameProcess.setText(_translate("MainWindow", "CHANGING"))
                        self.NameProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(230, 130, 255);}")
                        QtWidgets.QApplication.processEvents()
                        for item in self.Accounts:
                                name = self.InputName.text()
                                delay = self.InputTimeName.text()
                                print("SIGNING : "+str(item[2]))
                                self.tele_client = TelegramClient(item[2], item[0], item[1])
                                loop = asyncio.get_event_loop()
                                loop.run_until_complete(self.change_name_main(loop,name, item[2]))
                                time.sleep(int(delay))
                        # FINISH
                        self.NameProcess.setText(_translate("MainWindow", "FINISH"))
                        self.NameProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(255, 85, 0);}")
                        QtWidgets.QApplication.processEvents()
                        self.isRun = False
        def LeaveGroupFunc(self):
                if self.isRun == False:
                        self.isRun = True
                        _translate = QtCore.QCoreApplication.translate
                        self.JLProcess.setText(_translate("MainWindow", "STOP"))
                        self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(252, 234, 160);}")
                        QtWidgets.QApplication.processEvents()
                        self.JLProcess.setText(_translate("MainWindow", "LEAVING"))
                        self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(230, 130, 255);}")
                        # RUNING
                        for item in self.Accounts:
                                url  = self.InputURL.text()
                                delay = self.InputTimeJL.text()
                                print("SIGNING : "+str(item[2]))
                                self.tele_client = TelegramClient(item[2], item[0], item[1])
                                loop = asyncio.get_event_loop()
                                loop.run_until_complete(self.join_leave_channel_main(loop,url, item[2], 2))
                                time.sleep(int(delay))
                        # FINISH
                        QtWidgets.QApplication.processEvents()
                        self.JLProcess.setText(_translate("MainWindow", "FINISH"))
                        self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(255, 85, 0);}")
                        self.isRun = False
                        QtWidgets.QApplication.processEvents()
        def JoinGroupFunc(self):
                if self.isRun == False:
                        self.isRun = True
                        _translate = QtCore.QCoreApplication.translate
                        self.JLProcess.setText(_translate("MainWindow", "STOP"))
                        self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(252, 234, 160);}")
                        QtWidgets.QApplication.processEvents()
                        self.JLProcess.setText(_translate("MainWindow", "JOINING"))
                        self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(230, 130, 255);}")
                        # RUNING
                        for item in self.Accounts:
                                url  = self.InputURL.text()
                                delay = self.InputTimeJL.text()
                                print("SIGNING : "+str(item[2]))
                                self.tele_client = TelegramClient(item[2], item[0], item[1])
                                loop = asyncio.get_event_loop()
                                loop.run_until_complete(self.join_leave_channel_main(loop,url, item[2], 1))
                                time.sleep(int(delay))
                        # FINISH
                        QtWidgets.QApplication.processEvents()
                        self.JLProcess.setText(_translate("MainWindow", "FINISH"))
                        self.JLProcess.setStyleSheet("QPushButton{ border:0px;background:rgb(255, 85, 0);}")
                        self.isRun = False
                        QtWidgets.QApplication.processEvents()
        def addAccBlock(self,content):
                # ADD A USER GROUP (PHONE - APPID - APIHASH)
                usergroup = QtWidgets.QHBoxLayout()
                usergroup.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
                usergroup.setObjectName("UserGroup")
                phone = QtWidgets.QLineEdit(self.ListUserScrollContent)
                phone.setText(str(content[2])[0:5]+"xxxxxx")
                phone.setMaximumWidth(150)
                usergroup.addWidget(phone)
                app_id = QtWidgets.QLineEdit(self.ListUserScrollContent)
                app_id.setText(str(content[0]))
                phone.setMaximumWidth(100)
                usergroup.addWidget(app_id)
                hash_id = QtWidgets.QLineEdit(self.ListUserScrollContent)
                hash_id.setText(str(content[1])[0:5]+"xxxxxxxxxxxxxxxxx")
                usergroup.addWidget(hash_id)
                self.verticalLayout_2.addLayout(usergroup)
                # 
        def addLog(self,log_text):
                log_group = QtWidgets.QHBoxLayout()
                log_group.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
                self.verticalLayout_3.addLayout(log_group)
                log = QtWidgets.QLineEdit(self.LogScrollContentBlog)
                font = QtGui.QFont()
                font.setPointSize(12)
                log.setFont(font)
                log.setStyleSheet("QLineEdit{background:transparent;border:0px;}")
                log.setText(log_text)
                log_group.addWidget(log)
        def loadAccount(self):
                self.Accounts = ReadAccountList()
                for item in self.Accounts:
                        self.addAccBlock(item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setevent(MainWindow)
    ui.loadAccount()
    MainWindow.show()
    sys.exit(app.exec_())
