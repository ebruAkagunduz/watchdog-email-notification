#!/usr/bin/python
import sys
import git
import time
import subprocess

from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer

class FileEventHandler(PatternMatchingEventHandler):

    path = "/etc/"
            
    def on_any_event(self, event):
        print event
    

if __name__ == "__main__": 

    observer = Observer()
    event_handler = FileEventHandler(ignore_patterns=['*.swp', '*.swx', '*.swpx', '*~', '*.py'])
    observer.schedule(event_handler, FileEventHandler.path, recursive=True) 
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


