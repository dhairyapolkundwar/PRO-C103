import sys
import os
import time
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = input("Enter Directory To Start Observing Events Of >> ")

class EventArgs(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path + " has been created.")

    def on_deleted(self, event):
        print(event.src_path + " has been deleted.")
    
    def on_modified(self, event):
        print(event.src_path + " has been modified.")

    def on_moved(self, event):
        print(event.src_path + " has been moved.")

    def on_opened(self, event):
        print(event.src_path + " has been opened.")

    def on_closed(self, event):
        print(event.src_path + " has been closed.")



fileEventArgs = EventArgs()
inspector = Observer()

inspector.schedule(fileEventArgs, from_dir, recursive=True)

inspector.start()

try:
    while True:
        print("Observer Running...")
        time.sleep(1)
except KeyboardInterrupt:
    inspector.stop()
    print("Observer Stopped")
