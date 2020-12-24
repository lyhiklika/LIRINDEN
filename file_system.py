import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import datetime

global load
load = []

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        event.time = datetime.datetime.now()
        event.last = event.src_path.rfind('\\')
        load.append(event)
        

    def on_deleted(self, event):
        event.time = datetime.datetime.now()
        event.last = event.src_path.rfind('\\')
        load.append(event)

    def on_moved(self, event):
        event.time = datetime.datetime.now()
        event.last = event.src_path.rfind('\\')
        load.append(event)

    def on_modified(delf, event):
        event.time = datetime.datetime.now()
        event.last = event.src_path.rfind('\\')
        load.append(event)


def start():
    global observer
    observer = Observer()
    observer.schedule(Handler(), path=r"C:", recursive=True)
    observer.start()

def stop():
    try:
        observer.stop()
        observer.join()
    except:
        print('Запись не запущена')

def logs():
    return load
