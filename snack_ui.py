#imports dependencies
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
# initializes the application, you only need 1 per app.
app = QApplication([])
# makes a window for the application.
window = QWidget()

#declares variables for our UI 
total=QLineEdit('your total is')
grid_layout = QGridLayout()

charge=QPushButton('charge')
total=QLineEdit()
total.setText('total')
total.setEnabled(False)
total.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
window.setStyleSheet("""
	.QLineEdit {
		border-style: none;
		color: black;
		background:transparent;
		qproperty-iconSize: 10px 10px;
		}
	""")

cancel=QPushButton('cancel')

# tells python to use the grid layout class.
grid_layout.setSpacing(10)
grid_layout.addWidget(charge, 1,0)
grid_layout.addWidget(cancel, 1,3)
grid_layout.addWidget(total, 2,6)

#QListWidget for displaying snack list at checkout
#adds dictionary for generation of snack buttons.  
snacks=QListWidget()
popcorn={ 'name': 'popcorn', 'type': 'snack', 'cost': '0.25',}
button=""
for key in popcorn:
	button=button+str(popcorn[key])
snack_buttons=QPushButton(button)
grid_layout.addWidget(snack_buttons)

pop={ 'name': 'pop', 'type': 'drink', 'cost': '0.50',}
p_button=""
for key in pop:
 	p_button=p_button+str(pop[key])
p_button=QPushButton(p_button)
grid_layout.addWidget(p_button)

# code which is needed to exit any app.
window.setLayout(grid_layout)
window.show()
app.exec_()
