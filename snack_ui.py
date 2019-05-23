#imports dependencies
from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout  ,QPushButton, QLineEdit,QListWidget,QListWidgetItem, QListView
# initializes the application, you only need 1 per app.
app = QApplication([])
# makes a window for the application.
window = QWidget()

#declares variables for our UI 
total=QLineEdit('your total is')
charge=QPushButton('charge')
cancel=QPushButton('cancel')

# tells python to use the grid layout class.
grid_layout = QGridLayout()
grid_layout.setSpacing(10)
grid_layout.addWidget(charge, 1,0)
grid_layout.addWidget(cancel, 1,3)
grid_layout.addWidget(total, 1,2)

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
`grid_layout.addWidget(p_button)

# code which is needed to exit any app.
window.setLayout(grid_layout)
window.show()
app.exec_()
