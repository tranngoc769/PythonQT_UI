
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

list_accs = ReadAccountList()
for item in list_accs:
    tele_client = TelegramClient(item[2], item[1],item[0])
    print(item[2])
    tele_client.start()
    break