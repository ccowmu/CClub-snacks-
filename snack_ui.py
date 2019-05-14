# to run make sure you are in the right directory and type test.py you should now have a window.
# imports the application, the layout, the controls like buttons, and the widgets.      
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QLineEdit,QListWidget,QListWidgetItem
# inicializes the application, you only need 1 per app.
app = QApplication([])
# makes a window for the application.
window = QWidget()
# tells python we want to use the Vbox layout for our controls.
layout = QVBoxLayout()
# adds  buttons and other UI elements to the app.

layout.addWidget(QPushButton('charge'))
layout.addWidget(QLineEdit(' your total is '))
layout.addWidget(QPushButton('cancel'))
# sets the window 
window.setLayout(layout)
# shows the window on screen. Without this you will have no window for your application. 
window.show()
app.exec_()

