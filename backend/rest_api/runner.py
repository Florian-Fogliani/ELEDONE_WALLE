import threading
import time
from .variables import waiting_time, is_running, thread


def worker():
    global is_running
    while is_running:
        time.sleep((waiting_time - 500) / 1000)

def start():
    global is_running, thread
    if not is_running:
        is_running = True
        _thread = threading.Thread(target=worker, daemon=True)
        _thread.start()

def stop():
    global is_running
    is_running = False
