import ctypes
import time

while True:
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    time.sleep(3)