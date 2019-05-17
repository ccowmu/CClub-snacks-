# to run make sure you are in the right directory and type test.py you should now have a window.
# imports the application, the layout, the controls like buttons, and the widgets.      
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QLineEdit,QListWidget,QListWidgetItem, QListView
# initializes the application, you only need 1 per app.
app = QApplication([])
# makes a window for the application.
window = QWidget()
# tells python we want to use the Vbox layout for our controls.
layout = QVBoxLayout()
# adds  buttons and other UI elements to the app.

#QListWidget for displaying snack list at checkout
snack_checkout = QListWidget()

snack_checkout.addItem("Hershey's bar")
snack_checkout.addItem("Hershey's bar")
snack_checkout.addItem("M&Ms")
snack_checkout.addItem("Mountain Dew")

snack_checkout.setWindowTitle('Total Snack Purchase(s)')

layout.addWidget(QPushButton('charge'))
layout.addWidget(QLineEdit(' your total is '))
layout.addWidget(QPushButton('cancel'))
# sets the window 
window.setLayout(layout)
# shows the window on screen. Without this you will have no window for your application. 
window.show()
app.exec_()
