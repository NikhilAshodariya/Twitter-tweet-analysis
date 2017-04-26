import sys

sys.path.insert(1, '../View')
sys.path.insert(0, '../Model')

from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QInputDialog,QApplication)
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# import matplotlib.pyplot as plt


import useGUI
import twitter_Analysis

consumer_key='x9om0iHAuB8OnddJ4Zo0jhncw'
consumer_secret='epn4Y2OIwOaGHeM4GWZpodvwhNK8JMMSkDdsWKhrj3gDNQPf8g'
akey='856217924473958401-EdtIZi9fnOQ8ga6GV3uE2iGgqjZOCX7'
asecret='x5XmxzkgL1Eh66oxIcqmfpzaJYJcZRWBbU2zhPcv7bTQ2'


class Application:
	def __init__(self):

		# Creating View object
		GUIobj=useGUI.GUI()
		self.GUIobj=GUIobj

		# Creating Model object of Listener
		self.nikhilListener=twitter_Analysis.Listener() # This listener is of twitter_Analysis

		self.initGUI()
		self.configureElements()
		pass

	def initGUI(self):

		global consumer_key
		global consumer_secret
		global akey
		global asecret

		
		# Authorizing
		self.auth=OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(akey, asecret)

		self.twitterStream=Stream(self.auth, self.nikhilListener)
		pass

	def configureElements(self):
		# self.GUIobj.ui.searchButton.clicked.connect(self.otherSearch)
		self.GUIobj.ui.calc.clicked.connect(self.calculate)
		pass


	def calculate(self):
		string=str(self.GUIobj.ui.searchName.toPlainText())
		print('To search = ',string)
		self.twitterStream.filter(track=['string'])
		pass

	def otherSearch(self):
		self.GUIobj.ui.searchName.setPlainText('')
		self.nikhilListener.clearPlot()

