from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QRadioButton,QGroupBox,QHBoxLayout, QButtonGroup 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600, 400)
lbl = QLabel('Какой национальности не существует?')
btn = QPushButton('Ответить')
box = QGroupBox('Варианты ответов')
btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')
vlbox = QVBoxLayout()
hlbox1 = QHBoxLayout()
hlbox2 = QHBoxLayout()
hlbox1.addWidget(btn1)
hlbox1.addWidget(btn2)
hlbox2.addWidget(btn3)
hlbox2.addWidget(btn4)
vlbox.addLayout(hlbox1)
vlbox.addLayout(hlbox2)
box.setLayout(vlbox)


RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

lbl1 = QLabel('Правильно/Неправильно')
lbl2 = QLabel('Правильный ответ')
box2 = QGroupBox('Результат теста')
layout1 = QVBoxLayout()
layout1.addWidget(lbl1)
layout1.addWidget(lbl2)
box2.setLayout(layout1)



layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lbl)
layout_line2.addWidget(box)
layout_line2.addWidget(box2)
box2.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn, stretch=3)
layout_line3.addStretch(1)
vl = QVBoxLayout()
vl.addLayout(layout_line1, stretch=2)
vl.addLayout(layout_line2, stretch=8)
vl.addStretch(stretch=1)
vl.addLayout(layout_line3, stretch=1)
vl.addStretch(stretch = 1)
main_win.setLayout(vl)


def show_question():
    box2.hide()
    box.show
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    box.hide()
    box2.show()
    btn.setText('Следующий вопрос')




answers = [btn1, btn2, btn3, btn4]


def ask(q: Question):
    shuffle(answers)
    lbl.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl2.setText(q.right_answer)
    show_question()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')

def show_correct(res):
    lbl1.setText(res)
    show_result()

q = Question('два плюс два','четыре','хз','два','десять')
ask(q)
btn.clicked.connect(check_answer)

main_win.show()
app.exec_()