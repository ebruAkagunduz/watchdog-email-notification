#!/usr/bin/python
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

    path = "/etc/"
  
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
    event_handler = FileEventHandler(ignore_patterns=['*.swp', '*.swx', '*.swpx', '*~'])
    observer.schedule(event_handler, FileEventHandler.path, recursive=True) 
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


