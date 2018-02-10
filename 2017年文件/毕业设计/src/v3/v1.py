# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.ui'
#
# Created: Sat Mar 11 17:20:55 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from conf_data import conf_data
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object): 
    def icansee(me): 
         conf = conf_data() 
         conf.a0 = me.a0.text()   
         conf.a1 = me.a1.text()
         conf.b0 = me.b0.text()   
         conf.b1 = me.b1.text()  
         conf.width = me.width.text()  
         conf.height = me.height.text()  
         conf.threshold = me.horizontalSlider.value()
         conf.save()
    def set_value(self): 
         conf = conf_data()  
         self.a0.setText("%d" % conf.a0) 
         self.a1.setText("%d" % conf.a1)
         self.b0.setText("%d" % conf.b0)
         self.b1.setText("%d" % conf.b1)
         self.width.setText("%d" % conf.width)
         self.height.setText("%d" % conf.height)
         self.horizontalSlider.setValue(conf.threshold)


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(744, 604)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(520, 570, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalSlider = QtGui.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 450, 361, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.a0 = QtGui.QLineEdit(Dialog)
        self.a0.setGeometry(QtCore.QRect(577, 90, 41, 20))
        self.a0.setObjectName(_fromUtf8("a0"))
        self.b0 = QtGui.QLineEdit(Dialog)
        self.b0.setGeometry(QtCore.QRect(580, 160, 41, 20))
        self.b0.setObjectName(_fromUtf8("b0"))
        self.width = QtGui.QLineEdit(Dialog)
        self.width.setGeometry(QtCore.QRect(150, 340, 113, 20))
        self.width.setObjectName(_fromUtf8("width"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 420, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 90, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(470, 160, 111, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.height = QtGui.QLineEdit(Dialog)
        self.height.setGeometry(QtCore.QRect(470, 340, 113, 20))
        self.height.setObjectName(_fromUtf8("height"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 350, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(380, 350, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.threshold = QtGui.QLCDNumber(Dialog)
        self.threshold.setGeometry(QtCore.QRect(480, 450, 121, 23))
        self.threshold.setObjectName(_fromUtf8("threshold"))
        self.label_show = QtGui.QLabel(Dialog)
        self.label_show.setGeometry(QtCore.QRect(70, 30, 311, 221))
        self.label_show.setText(_fromUtf8(""))
        self.label_show.setObjectName(_fromUtf8("label_show"))
        self.draw_line = QtGui.QPushButton(Dialog)
        self.draw_line.setGeometry(QtCore.QRect(470, 260, 75, 23))
        self.draw_line.setObjectName(_fromUtf8("draw_line"))
        self.a1 = QtGui.QLineEdit(Dialog)
        self.a1.setGeometry(QtCore.QRect(650, 90, 41, 20))
        self.a1.setObjectName(_fromUtf8("a1"))
        self.b1 = QtGui.QLineEdit(Dialog)
        self.b1.setGeometry(QtCore.QRect(650, 160, 41, 20))
        self.b1.setObjectName(_fromUtf8("b1"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.icansee)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.threshold.display)
        QtCore.QObject.connect(self.draw_line, QtCore.SIGNAL(_fromUtf8("clicked()")), self.icansee)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.horizontalSlider, self.a0)
        Dialog.setTabOrder(self.a0, self.b0)
        Dialog.setTabOrder(self.b0, self.width)
        Dialog.setTabOrder(self.width, self.height)
        Dialog.setTabOrder(self.height, self.buttonBox)
        self.set_value()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "灵敏度", None))
        self.label_2.setText(_translate("Dialog", "投影左上角", None))
        self.label_5.setText(_translate("Dialog", "投影右下角", None))
        self.label_6.setText(_translate("Dialog", "宽度", None))
        self.label_7.setText(_translate("Dialog", "高度", None))
        self.draw_line.setText(_translate("Dialog", "检测", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

