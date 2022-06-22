#! /Users/liamcunliffe/.pyenv/shims/python

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
import subprocess
from time import localtime, strftime
import os
import json

class MyHandler(FileSystemEventHandler):
  i = 1
  def on_modified(self, event):
    for filename in os.listdir(folder_to_track):
      src = folder_to_track + "/" + filename
      file_extention = filename.rsplit(".",1)[1].lower()
      new_destination = self.organise_file(filename, file_extention)
      os.rename(src, new_destination)
      dest_folder = new_destination.rsplit("/")[-2]
      filename = filename[:20] + "..."
      if(filename != ".DS_Store"):
        notification_message = filename + " moved to " + dest_folder
        apple_cmd = "osascript -e '{0}'".format('display notification "File Automator" with title "{0}" sound name "Purr"').format(notification_message)
        subprocess.Popen([apple_cmd], shell=True)
        print("\n" + filename + " moved to " + dest_folder + " at " + strftime("%Y-%m-%d %H:%M:%S", localtime()))
            
  def organise_file(self, filename, file_extention):
    file_location = '/Users/liamcunliffe/Library/Mobile Documents/com~apple~CloudDocs/Downloads/'

    if(file_extention == 'pdf'):

      new_destination = file_location + 'PDFs/' + filename

    elif(file_extention == "jpg" or 
          file_extention == "jpeg" or 
            file_extention == "png" or 
                file_extention == "gif" or 
                    file_extention == "tiff"):

      new_destination = file_location + 'Images/' + filename

    elif(file_extention == "doc" or 
          file_extention == "docx" or 
              file_extention == "xlsx" or 
                  file_extention == "xls" or 
                      file_extention == "ppt" or
                          file_extention == "pptx"):
            
      new_destination = file_location + 'Office Files/' + filename

    elif(file_extention == "mov" or 
          file_extention == "mpg" or 
            file_extention == "mp4" or 
              file_extention == "flv" or 
                  file_extention == "webm" or 
                      file_extention == "wmv"):

      new_destination = file_location + 'Videos/' + filename

    elif(file_extention == "dmg" or 
          file_extention == "pkg"):

      new_destination = file_location + 'Software/' + filename

    elif(file_extention == "txt" or
          file_extention == "rtf" or
              file_extention == "pages" or
                  file_extention == "text"):
        
      new_destination = file_location + 'Text Files/' + filename

    elif(file_extention == "py" or
          file_extention == "c" or
              file_extention == "cpp" or
                  file_extention == "java" or
                      file_extention == "js" or
                          file_extention == "cs" or
                              file_extention == "class" or
                                  file_extention == "dtd" or
                                      file_extention == "xml" or
                                          file_extention == "html" or
                                              file_extention == "htm" or
                                                  file_extention == "css" or
                                                      file_extention == "json" or
                                                          file_extention == "sql"):

      new_destination = file_location + 'Code Files/' + filename

    elif(file_extention == "7z" or
          file_extention == "zip" or
              file_extention == "zipx" or
                  file_extention == "tar.gz" or
                      file_extention == "rar" or
                          file_extention == "cbr"):
        
      new_destination = file_location + 'Compressed/' + filename

    elif(file_extention == "mp3" or
          file_extention == "wav" or
              file_extention == "pmc" or
                  file_extention == "aiff" or
                      file_extention == "aac" or
                          file_extention == "ogg"):
        
      new_destination = file_location + 'Audio/' + filename

    else:
      
      new_destination = file_location + 'Miscellaneous/' + filename

    return new_destination

folder_to_track = '/Users/liamcunliffe/Desktop/'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()

observer.join()
