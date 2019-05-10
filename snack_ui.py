# to run make sure you are in the right directory and type test.py you should now have a window.
# imports the application, the layout, the controls like buttons, and the widgets.      
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout,QPushButton, QLineEdit 
# inicializes the application, you only need 1 per app.
app = QApplication([])
#  don't remove this line or else Orka will break!!
# makes a window for the application.
window = QWidget()
# tells python we want to use the Vbox layout for our controls.
layout = QVBoxLayout()
# adds a button. 
layout.addWidget(QPushButton('clear'))
layout.addWidget(QPushButton('charge')) 
layout.addWidget(QLineEdit('total'))


# sets the window layout.
window.setLayout(layout)
# shows the window on screen. Without this you will have no window for your application. 
window.show()
# closes the app. If this statement isn't here, you will have an application which doesn't exit. 
app.exec_()

