#!/usr/bin/python
# -*- coding: utf-8; -*-

"""
Copyright (C) 2013 - Ebru Akagündüz <ebru.akagunduz@gmail.com>

This file is part of watchdog-email-notification.

watchdog-email-notification is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

watchdog-email-notification is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""


import sys
import git
import time
import smtplib
import subprocess

from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "user"
SMTP_PASSWORD = "passwd"
EMAIL_TO = "to"
EMAIL_FROM = "from"
EMAIL_SUBJECT = "Info from watchdog"
PATH = "/etc/"

class SendMail():

    def send_email(self, file_path):
        content = ''.join([file_path + " changed" + "\n\n" +
                  time.asctime(time.localtime(time.time()))])
        msg = MIMEText(content)
        msg['Subject'] = EMAIL_SUBJECT
        msg['To'] = EMAIL_TO
        msg['From'] = EMAIL_FROM
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        mail.starttls()
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        mail.quit()

class FileEventHandler(PatternMatchingEventHandler):

    def on_modified(self, event):
        obj = SendMail()
        obj.send_email(event.src_path)

    def on_moved(self, event):
        # if exist backup file
        if event.src_path + "~" == event.dest_path:
            return
        obj.send_email(event.src_path)
            
    def on_deleted(self, event):
        obj = SendMail()
        obj.send_email(event.src_path)
    
    def on_created(self, event):
        obj = SendMail()
        obj.send_email(event.src_path)
    

if __name__ == "__main__": 

    observer = Observer()
    event_handler = FileEventHandler(ignore_patterns=['*.swp', '*.swx', '*.swpx'])
    observer.schedule(event_handler, PATH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


