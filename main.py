# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(945, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_a = QtWidgets.QPushButton(self.centralwidget)
        self.button_a.setGeometry(QtCore.QRect(10, 160, 88, 34))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(149, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_a.setPalette(palette)
        self.button_a.setObjectName("button_a")
        self.label_odpowiedz_a = QtWidgets.QLabel(self.centralwidget)
        self.label_odpowiedz_a.setGeometry(QtCore.QRect(110, 170, 801, 18))
        self.label_odpowiedz_a.setObjectName("label_odpowiedz_a")
        self.label_odpowiedz_b = QtWidgets.QLabel(self.centralwidget)
        self.label_odpowiedz_b.setGeometry(QtCore.QRect(110, 250, 821, 18))
        self.label_odpowiedz_b.setObjectName("label_odpowiedz_b")
        self.button_b = QtWidgets.QPushButton(self.centralwidget)
        self.button_b.setGeometry(QtCore.QRect(10, 240, 88, 34))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(27, 116, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 116, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 116, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_b.setPalette(palette)
        self.button_b.setObjectName("button_b")
        self.button_c = QtWidgets.QPushButton(self.centralwidget)
        self.button_c.setGeometry(QtCore.QRect(10, 310, 88, 34))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 87, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 87, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 87, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_c.setPalette(palette)
        self.button_c.setObjectName("button_c")
        self.label_odpowiedz_c = QtWidgets.QLabel(self.centralwidget)
        self.label_odpowiedz_c.setGeometry(QtCore.QRect(110, 320, 781, 16))
        self.label_odpowiedz_c.setObjectName("label_odpowiedz_c")
        self.label_pytanie = QtWidgets.QLabel(self.centralwidget)
        self.label_pytanie.setGeometry(QtCore.QRect(180, 120, 741, 18))
        self.label_pytanie.setObjectName("label_pytanie")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 30, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_ocena = QtWidgets.QLabel(self.centralwidget)
        self.label_ocena.setGeometry(QtCore.QRect(10, 480, 851, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ocena.setFont(font)
        self.label_ocena.setObjectName("label_ocena")
        self.button_nastepne = QtWidgets.QPushButton(self.centralwidget)
        self.button_nastepne.setGeometry(QtCore.QRect(320, 600, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 153, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 153, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 153, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.button_nastepne.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_nastepne.setFont(font)
        self.button_nastepne.setAutoExclusive(False)
        self.button_nastepne.setObjectName("button_nastepne")
        self.label_wynik = QtWidgets.QLabel(self.centralwidget)
        self.label_wynik.setGeometry(QtCore.QRect(620, 530, 311, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(36, 106, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 106, 171))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 113, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 103, 104))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_wynik.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_wynik.setFont(font)
        self.label_wynik.setObjectName("label_wynik")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 0, 391, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kot.png"))
        self.label.setObjectName("label")
        self.label_dobre = QtWidgets.QLabel(self.centralwidget)
        self.label_dobre.setGeometry(QtCore.QRect(30, 520, 211, 221))
        self.label_dobre.setText("")
        self.label_dobre.setPixmap(QtGui.QPixmap("dobra.jpg"))
        self.label_dobre.setObjectName("label_dobre")
        self.label_zla = QtWidgets.QLabel(self.centralwidget)
        self.label_zla.setGeometry(QtCore.QRect(20, 530, 261, 191))
        self.label_zla.setText("")
        self.label_zla.setPixmap(QtGui.QPixmap("zla.jpg"))
        self.label_zla.setObjectName("label_zla")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_a.setText(_translate("MainWindow", "A"))
        self.label_odpowiedz_a.setText(_translate("MainWindow", "A"))
        self.label_odpowiedz_b.setText(_translate("MainWindow", "B"))
        self.button_b.setText(_translate("MainWindow", "B"))
        self.button_c.setText(_translate("MainWindow", "C"))
        self.label_odpowiedz_c.setText(_translate("MainWindow", "C"))
        self.label_pytanie.setText(_translate("MainWindow", "PYTANIE"))
        self.label_5.setText(_translate("MainWindow", "WWW.quiz.pl"))
        self.label_ocena.setText(_translate("MainWindow", " poprawna odpowiedż to"))
        self.button_nastepne.setText(_translate("MainWindow", "następne pytanie "))
        self.label_wynik.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
