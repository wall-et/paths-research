import logging
from PyQt5 import QtWidgets,uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("main.ui")

# from paths.view import View


from PyQt5 import QtWidgets, uic

def run():
   f = win.firstname.lineEdit_item.text()
   print(f)
   # f = win.firstname.text()
   # i = win.secondname.text()
   print(f)
   # print(i)
#
# v = View()
#
#
# v.start()
#
app = QtWidgets.QApplication([])
win = uic.loadUi("main.ui")
win.BTlaod.clicked.connect(run)
win.show()

#
#
# class Convert(QMainWindow):
#     def __init__(self):
#         super(Convert,self).__init__()
#         # self.title = 'PyQt5 button - pythonspot.com'
#         # self.left = 10
#         # self.top = 10
#         # self.width = 320
#         # self.height = 200
#         # self.initUI()
#
#     def initUI(self):
#         # self.setWindowTitle(self.title)
#         # self.setGeometry(self.left, self.top, self.width, self.height)
#
#         button = QPushButton(dlg.BTlaod, self)
#         button.setToolTip('This is an example button')
#         button.move(100, 70)
#         # dlg.BTlaod.clicked.connect(self.on_click)
#         dlg.BTlaod.clicked.connect(self.on_click)
#         # f = button.clicked.connect(self.on_click)
#         # print(f)
#
#     @pyqtSlot()
#     def on_click(self):
#         self.label.setText("Button Clicked")
#         print('PyQt5 button click')

dlg.show()
app.exec()


