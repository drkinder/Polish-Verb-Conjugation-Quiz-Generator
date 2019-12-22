import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from quiz_generator import QuizGenerator


class QuizWindow(QtWidgets.QMainWindow):
    
    def __init__(self, filtering, quiz_length):
        super(QuizWindow, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Polish Conjugations")
        
        self.verb_data_label = QtWidgets.QLabel(self)
        self.verb_data_label.move(10, 10)
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.move(130, 105)  
        self.scoreLabel = QtWidgets.QLabel(self)
        self.scoreLabel.move(10, 150)
        
        self.quiz = QuizGenerator(filtering, quiz_length)
        self.question_dict = self.quiz.generate_questions()
        self.question_list = []
        for question in self.question_dict:
            self.question_list.append(question)
        
        self.index = 0  # Begin with first verb in question_list
        self.number_correct = 0
        self.quiz_page()
        
    def quiz_page(self):
        
        self.verb_data_label.setText(self.question_list[self.index] + " :")
        self.verb_data_label.setFont(QtGui.QFont('Arial', 10))
        self.verb_data_label.resize(300, 20)
        
        self.inputbox = QtWidgets.QLineEdit(self)
        self.inputbox.move(10, 50)
        self.inputbox.resize(250, 40)
        
        self.check_answer_btn = QtWidgets.QPushButton("Submit Answer", self)
        self.check_answer_btn.clicked.connect(self.check_answer)
        self.check_answer_btn.setDefault(True)
        self.check_answer_btn.move(10, 100)
        self.show()
        
    def check_answer(self):
        answer = self.inputbox.text()
        if self.question_dict[self.question_list[self.index]] == answer:
            self.number_correct += 1
            label_text = "Correct!"
        else:
            label_text = "Wrong: {}".format(self.question_dict[self.question_list[self.index]])
        
        self.result_label.setText(label_text)
        self.result_label.setFont(QtGui.QFont('Arial', 10))
        self.result_label.resize(150, 20)
        
        if len(self.question_list)-1 > self.index:
            self.index += 1
            
            self.verb_data_label.setText(self.question_list[self.index] + " :")
            self.inputbox.clear()
        else:      
            
            self.check_answer_btn.setEnabled(False)
            self.scoreLabel.setText("{}/{} Correct!".format(self.number_correct,
                                                            len(self.question_list)))
            self.scoreLabel.setFont(QtGui.QFont('Arial', 20))
            self.scoreLabel.resize(300, 30)
            print("FINISHED")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = QuizWindow({"present": ["ja"]}, 3)
    sys.exit(app.exec_())
