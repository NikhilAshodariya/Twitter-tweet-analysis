import sys
from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QInputDialog,QApplication)
# from GUI import Ui_TweetAnalysis
from GUI import Ui_TweetAnalysis


class GUI(QWidget):

	def __init__(self):
		super().__init__()
		self.initGUI()
		print('setup clear')
		self.show()

	def initGUI(self):
		self.ui=Ui_TweetAnalysis()
		self.ui.setupUi(self)
		self.configureElements()
		# self.show()

	def configureElements(self):
		self.ui.quit.clicked.connect(self.quitFunction)


	def quitFunction(self):
		sys.exit(0)

	def otherSearch(self):
		self.ui.searchName.setPlainText('')

		# make the graph also to reset



