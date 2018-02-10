import sys
import cv2
from PyQt4 import phonon
from PyQt4 import QtCore, QtGui
from v1 import Ui_Dialog
from conf_data import conf_data
#import threading



img = cv2.imread('1.jpg')
app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)

image = cv2.imread("1.jpg") 
image = cv2.resize(image, (300,225), interpolation=cv2.INTER_AREA) 
#conf = conf_data()  
#a0=conf.a0
#a1=conf.a1
#b0=conf.b0
#b1=conf.b1
#print b1
#cv2.rectangle(image,(a0,a1),(b0,b1),(55,255,155),5)
frame = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)  
ui.label_show.setPixmap(QtGui.QPixmap.fromImage(frame))


#def func():
  #print conf_data.threshold
#timer = threading.Timer(5, func)
#timer.start()

Dialog.show()
sys.exit(app.exec_())

