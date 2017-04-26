import sys

# sys.path.insert(0, 'Controller')

from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QInputDialog,QApplication)


import Run


app=QApplication(sys.argv)
ex=Run.Application()
ex.GUIobj.show()
sys.exit(app.exec_())