from PyQt5 import QtCore, QtGui, QtWidgets
from quiz_window import QuizWindow


class UIMainWindow:
    
    def main(self):
        self.window = QtWidgets.QMainWindow()
        filtering = self.build_filtering()
        quiz_length = int(str(self.quizLengthComboBox.currentText()))
        self.ui = QuizWindow(filtering, quiz_length)
        
    def build_filtering(self):
        filtering = {}
        if self.presentTenseCheckBox.isChecked():
            filtering["present"] = []
            if self.present1sCheckBox.isChecked():
                filtering["present"].append("ja")
            if self.present2sCheckBox.isChecked():
                filtering["present"].append("ty")
            if self.present3sCheckBox.isChecked():
                filtering["present"].append("on/ona")
            if self.present1pCheckBox.isChecked():
                filtering["present"].append("my")
            if self.present2pCheckBox.isChecked():
                filtering["present"].append("wy")
            if self.present3pCheckBox.isChecked():
                filtering["present"].append("oni/one")
            if len(filtering["present"]) == 0:
                filtering.pop("present")
                
        if self.pastMascTenseCheckBox.isChecked():
            filtering["past_masc"] = []
            if self.pastMasc1sCheckBox.isChecked():
                filtering["past_masc"].append("ja")
            if self.pastMasc2sCheckBox.isChecked():
                filtering["past_masc"].append("ty")
            if self.pastMasc3sCheckBox.isChecked():
                filtering["past_masc"].append("on")
            if self.pastMasc1pCheckBox.isChecked():
                filtering["past_masc"].append("my")
            if self.pastMasc2pCheckBox.isChecked():
                filtering["past_masc"].append("wy")
            if self.pastMasc3pCheckBox.isChecked():
                filtering["past_masc"].append("oni")
            if len(filtering["past_masc"]) == 0:
                filtering.pop("past_masc")
                
        if self.pastFemTenseCheckBox.isChecked():
            filtering["past_fem"] = []
            if self.pastFem1sCheckBox.isChecked():
                filtering["past_fem"].append("ja")
            if self.pastFem2sCheckBox.isChecked():
                filtering["past_fem"].append("ty")
            if self.pastFem3sCheckBox.isChecked():
                filtering["past_fem"].append("ona")
            if self.pastFem1pCheckBox.isChecked():
                filtering["past_fem"].append("my")
            if self.pastFem2pCheckBox.isChecked():
                filtering["past_fem"].append("wy")
            if self.pastFem3pCheckBox.isChecked():
                filtering["past_fem"].append("one")
            if len(filtering["past_fem"]) == 0:
                filtering.pop("past_fem")
                
        return filtering
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 575)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        #Present Tense
        self.presentTenseCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.presentTenseCheckBox.setGeometry(QtCore.QRect(40, 50, 191, 20))
        self.presentTenseCheckBox.setObjectName("presentTenseCheckBox")
        
        self.present1sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.present1sCheckBox.setGeometry(QtCore.QRect(70, 80, 81, 20))
        self.present1sCheckBox.setObjectName("present1sCheckBox")
        self.present1sCheckBox.setEnabled(False)
        
        self.present2sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.present2sCheckBox.setGeometry(QtCore.QRect(160, 80, 81, 20))
        self.present2sCheckBox.setObjectName("present2sCheckBox")
        self.present2sCheckBox.setEnabled(False)        
        
        self.present3sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.present3sCheckBox.setGeometry(QtCore.QRect(250, 80, 81, 20))
        self.present3sCheckBox.setObjectName("present3sCheckBox")
        self.present3sCheckBox.setEnabled(False)       
  
        self.present1pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.present1pCheckBox.setGeometry(QtCore.QRect(340, 80, 81, 20))
        self.present1pCheckBox.setObjectName("present1pCheckBox")
        self.present1pCheckBox.setEnabled(False)
        
        self.present2pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.present2pCheckBox.setGeometry(QtCore.QRect(430, 80, 81, 20))
        self.present2pCheckBox.setObjectName("present2pCheckBox")
        self.present2pCheckBox.setEnabled(False)
        
        self.present3pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.present3pCheckBox.setGeometry(QtCore.QRect(520, 80, 81, 20))
        self.present3pCheckBox.setObjectName("present3pCheckBox")
        self.present3pCheckBox.setEnabled(False)      
        
        self.presentTenseCheckBox.toggled.connect(self.handle_present_subjects)
        
        #Past Tense Masc
        self.pastMascTenseCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMascTenseCheckBox.setGeometry(QtCore.QRect(40, 120, 191, 20))
        self.pastMascTenseCheckBox.setObjectName("pastMascTenseCheckBox")
        
        self.pastMasc1sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMasc1sCheckBox.setGeometry(QtCore.QRect(70, 150, 81, 20))
        self.pastMasc1sCheckBox.setObjectName("pastMasc1sCheckBox")
        self.pastMasc1sCheckBox.setEnabled(False)
        
        self.pastMasc2sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMasc2sCheckBox.setGeometry(QtCore.QRect(160, 150, 81, 20))
        self.pastMasc2sCheckBox.setObjectName("pastMasc2sCheckBox")
        self.pastMasc2sCheckBox.setEnabled(False)
        
        self.pastMasc3sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMasc3sCheckBox.setGeometry(QtCore.QRect(250, 150, 81, 20))
        self.pastMasc3sCheckBox.setObjectName("pastMasc3sCheckBox")
        self.pastMasc3sCheckBox.setEnabled(False)        
        
        self.pastMasc1pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMasc1pCheckBox.setGeometry(QtCore.QRect(340, 150, 81, 20))
        self.pastMasc1pCheckBox.setObjectName("pastMasc1pCheckBox")
        self.pastMasc1pCheckBox.setEnabled(False)
        
        self.pastMasc2pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMasc2pCheckBox.setGeometry(QtCore.QRect(430, 150, 81, 20))
        self.pastMasc2pCheckBox.setObjectName("pastMasc2pCheckBox")
        self.pastMasc2pCheckBox.setEnabled(False)
        
        self.pastMasc3pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastMasc3pCheckBox.setGeometry(QtCore.QRect(520, 150, 81, 20))
        self.pastMasc3pCheckBox.setObjectName("pastMasc3pCheckBox")
        self.pastMasc3pCheckBox.setEnabled(False)
        
        self.pastMascTenseCheckBox.toggled.connect(self.handle_pastm_subjects)
        
        #Past Tense Fem
        self.pastFemTenseCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFemTenseCheckBox.setGeometry(QtCore.QRect(40, 190, 191, 20))
        self.pastFemTenseCheckBox.setObjectName("pastFemTenseCheckBox")
        
        self.pastFem1sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFem1sCheckBox.setGeometry(QtCore.QRect(70, 220, 81, 20))
        self.pastFem1sCheckBox.setObjectName("pastMasc1sCheckBox")
        self.pastFem1sCheckBox.setEnabled(False)
        
        self.pastFem2sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFem2sCheckBox.setGeometry(QtCore.QRect(160, 220, 81, 20))
        self.pastFem2sCheckBox.setObjectName("pastMasc2sCheckBox")
        self.pastFem2sCheckBox.setEnabled(False)
        
        self.pastFem3sCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFem3sCheckBox.setGeometry(QtCore.QRect(250, 220, 81, 20))
        self.pastFem3sCheckBox.setObjectName("pastMasc3sCheckBox")
        self.pastFem3sCheckBox.setEnabled(False)        
        
        self.pastFem1pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFem1pCheckBox.setGeometry(QtCore.QRect(340, 220, 81, 20))
        self.pastFem1pCheckBox.setObjectName("pastMasc1pCheckBox")
        self.pastFem1pCheckBox.setEnabled(False)
        
        self.pastFem2pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFem2pCheckBox.setGeometry(QtCore.QRect(430, 220, 81, 20))
        self.pastFem2pCheckBox.setObjectName("pastMasc2pCheckBox")
        self.pastFem2pCheckBox.setEnabled(False)
        
        self.pastFem3pCheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.pastFem3pCheckBox.setGeometry(QtCore.QRect(520, 220, 81, 20))
        self.pastFem3pCheckBox.setObjectName("pastMasc3pCheckBox")
        self.pastFem3pCheckBox.setEnabled(False)
        
        self.pastFemTenseCheckBox.toggled.connect(self.handle_pastf_subjects)
        
        # Drop down menu - Quiz Length
        self.quizLengthComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.quizLengthComboBox.addItem("3")
        self.quizLengthComboBox.addItem("5")
        self.quizLengthComboBox.addItem("10")
        self.quizLengthComboBox.addItem("20")
        self.quizLengthComboBox.addItem("30")
        self.quizLengthComboBox.addItem("40")
        self.quizLengthComboBox.addItem("50")
        self.quizLengthComboBox.setGeometry(QtCore.QRect(680, 120, 93, 28))
        self.quizLengthComboBox.setObjectName("quizLengthComboBox")
        self.quizLengthComboBox.setCurrentIndex(1)
        
        self.quizLengthLabel = QtWidgets.QLabel(self.centralWidget)
        self.quizLengthLabel.setText("Quiz Length")
        self.quizLengthLabel.setGeometry(QtCore.QRect(680, 90, 93, 28))
        
        # Start Quiz Button
        self.startQuizButton = QtWidgets.QPushButton(self.centralWidget)
        self.startQuizButton.setGeometry(QtCore.QRect(680, 470, 93, 28))       
        self.startQuizButton.setObjectName("startQuizButton")
        self.startQuizButton.clicked.connect(self.main)
        
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 839, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.presentTenseCheckBox.setText(_translate("MainWindow", "Present Tense"))        
        self.present1sCheckBox.setText(_translate("MainWindow", "ja"))
        self.present2sCheckBox.setText(_translate("MainWindow", "ty"))
        self.present3sCheckBox.setText(_translate("MainWindow", "on/ona"))
        self.present1pCheckBox.setText(_translate("MainWindow", "my"))
        self.present2pCheckBox.setText(_translate("MainWindow", "wy"))
        self.present3pCheckBox.setText(_translate("MainWindow", "oni/one"))
        
        self.pastMascTenseCheckBox.setText(_translate("MainWindow", "Masculine Past Tense"))
        self.pastMasc1sCheckBox.setText(_translate("MainWindow", "ja"))
        self.pastMasc2sCheckBox.setText(_translate("MainWindow", "ty"))
        self.pastMasc3sCheckBox.setText(_translate("MainWindow", "on"))
        self.pastMasc1pCheckBox.setText(_translate("MainWindow", "my"))
        self.pastMasc2pCheckBox.setText(_translate("MainWindow", "wy"))
        self.pastMasc3pCheckBox.setText(_translate("MainWindow", "oni"))
        
        self.pastFemTenseCheckBox.setText(_translate("MainWindow", "Feminine Past Tense")) 
        self.pastFem1sCheckBox.setText(_translate("MainWindow", "ja"))
        self.pastFem2sCheckBox.setText(_translate("MainWindow", "ty"))
        self.pastFem3sCheckBox.setText(_translate("MainWindow", "ona"))
        self.pastFem1pCheckBox.setText(_translate("MainWindow", "my"))
        self.pastFem2pCheckBox.setText(_translate("MainWindow", "wy"))
        self.pastFem3pCheckBox.setText(_translate("MainWindow", "one"))
        
        self.startQuizButton.setText(_translate("MainWindow", "Generate Quiz"))
        #self.quizLengthComboBox.setText(_translate("MainWindow", "Quiz Length"))

    def handle_present_subjects(self):
        switch = self.presentTenseCheckBox.isChecked()
        self.present1sCheckBox.setChecked(switch)
        self.present1sCheckBox.setEnabled(switch)
        self.present2sCheckBox.setChecked(switch)
        self.present2sCheckBox.setEnabled(switch)
        self.present3sCheckBox.setChecked(switch)
        self.present3sCheckBox.setEnabled(switch)
        self.present1pCheckBox.setChecked(switch)
        self.present1pCheckBox.setEnabled(switch)
        self.present2pCheckBox.setChecked(switch)
        self.present2pCheckBox.setEnabled(switch)
        self.present3pCheckBox.setChecked(switch)
        self.present3pCheckBox.setEnabled(switch)
        
    def handle_pastm_subjects(self):
        switch = self.pastMascTenseCheckBox.isChecked()
        self.pastMasc1sCheckBox.setChecked(switch)
        self.pastMasc1sCheckBox.setEnabled(switch)
        self.pastMasc2sCheckBox.setChecked(switch)
        self.pastMasc2sCheckBox.setEnabled(switch)
        self.pastMasc3sCheckBox.setChecked(switch)
        self.pastMasc3sCheckBox.setEnabled(switch)
        self.pastMasc1pCheckBox.setChecked(switch)
        self.pastMasc1pCheckBox.setEnabled(switch)
        self.pastMasc2pCheckBox.setChecked(switch)
        self.pastMasc2pCheckBox.setEnabled(switch)
        self.pastMasc3pCheckBox.setChecked(switch)
        self.pastMasc3pCheckBox.setEnabled(switch) 
            
    def handle_pastf_subjects(self):
        switch = self.pastFemTenseCheckBox.isChecked()
        self.pastFem1sCheckBox.setChecked(switch)
        self.pastFem1sCheckBox.setEnabled(switch)
        self.pastFem2sCheckBox.setChecked(switch)
        self.pastFem2sCheckBox.setEnabled(switch)
        self.pastFem3sCheckBox.setChecked(switch)
        self.pastFem3sCheckBox.setEnabled(switch)
        self.pastFem1pCheckBox.setChecked(switch)
        self.pastFem1pCheckBox.setEnabled(switch)
        self.pastFem2pCheckBox.setChecked(switch)
        self.pastFem2pCheckBox.setEnabled(switch)
        self.pastFem3pCheckBox.setChecked(switch)
        self.pastFem3pCheckBox.setEnabled(switch)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

