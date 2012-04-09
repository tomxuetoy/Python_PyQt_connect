import sys
from PyQt4 import QtCore, QtGui


app = QtGui.QApplication(sys.argv)

quit = QtGui.QPushButton("Quit")
quit.resize(175, 130)
# below code completion by QtGui.QPushButton. & CTrl+x & Ctrl+o
quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"),
                       app, QtCore.SLOT("quit()"))

quit.show()
sys.exit(app.exec_()) 
