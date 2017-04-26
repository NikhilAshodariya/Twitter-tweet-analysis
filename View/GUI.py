from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TweetAnalysis(object):
    def setupUi(self, TweetAnalysis):
        TweetAnalysis.setObjectName("TweetAnalysis")
        TweetAnalysis.resize(513, 428)
        self.searchName = QtWidgets.QPlainTextEdit(TweetAnalysis)
        self.searchName.setGeometry(QtCore.QRect(50, 50, 431, 31))
        self.searchName.setObjectName("searchName")
        self.quit = QtWidgets.QPushButton(TweetAnalysis)
        self.quit.setGeometry(QtCore.QRect(70, 190, 80, 22))
        self.quit.setObjectName("quit")
        self.calc = QtWidgets.QPushButton(TweetAnalysis)
        self.calc.setGeometry(QtCore.QRect(210, 190, 80, 22))
        self.calc.setObjectName("calc")
        # self.searchButton = QtWidgets.QPushButton(TweetAnalysis)
        # self.searchButton.setGeometry(QtCore.QRect(359, 190, 91, 22))
        # self.searchButton.setObjectName("searchButton")

        self.retranslateUi(TweetAnalysis)
        QtCore.QMetaObject.connectSlotsByName(TweetAnalysis)

    def retranslateUi(self, TweetAnalysis):
        _translate = QtCore.QCoreApplication.translate
        TweetAnalysis.setWindowTitle(_translate("TweetAnalysis", "Tweet Analysis"))
        self.searchName.setPlainText(_translate("TweetAnalysis", ""))
        self.quit.setText(_translate("TweetAnalysis", "Quit"))
        self.calc.setText(_translate("TweetAnalysis", "Calculate"))
        # self.searchButton.setText(_translate("TweetAnalysis", "Other Search"))

