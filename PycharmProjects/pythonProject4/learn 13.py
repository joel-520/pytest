

from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import time
record = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
app = QApplication(sys.argv)
def timer(n):
    while True:
        dt= time.strftime('%Y-%m-%d %H%M%S',time.localtime())
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(record).toImage()
        img.save("D:\\images\\"+dt+".jpg")
        time.sleep(n)
if __name__ == "__main__":
    timer(2)
