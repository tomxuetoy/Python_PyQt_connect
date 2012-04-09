import sys
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)

quit = QtGui.QPushButton("Quit")

QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"),
                       app, QtCore.SLOT("quit()"))

quit.show()
sys.exit(app.exec_()) 
