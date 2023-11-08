from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from random import choice, shuffle
from time import sleep

app = QApplication([])

from card_window import *
from main_window import *

card_win.setWindowTitle("Memory card")


# клас для запитань
class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.is_asking = True
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1

# створення обєктів запитань
q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')
# списки з питаннями та кнопками
radio_buttons = [rbtn1, rbtn2, rbtn3, rbtn4]
questions = [q1, q2, q3, q4]

# функція яка рандомно генерує питання і відображає в картці
def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_correct.setText(cur_quest.answer)


    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_quest.wrong_ans1)
    radio_buttons[1].setText(cur_quest.wrong_ans2)
    radio_buttons[2].setText(cur_quest.wrong_ans3)
    radio_buttons[3].setText(cur_quest.answer)


new_question()
# функція яка перевіряє правильну відповідь
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lbl_correct.text():
                cur_quest.got_right()
                lbl_result.setText("Правильно!")
                answer.setChecked(False)
                break
    else:
        lbl_result.setText("Не правильно!")
        cur_quest.got_wrong()
    RadioGroup.setExclusive(True)

# функція яка перемикає питання
def switch_screen():
    if btn_ok.text() == 'Відповісти':
        check()
        RadioGroupBox.hide()
        AnsGroupBox.show()

        btn_ok.setText("Наступне запитання")
    else:
        new_question()
        AnsGroupBox.hide()
        RadioGroupBox.show()

        btn_ok.setText('Відповісти')

# функція яка зупиняє програму на заданий час
def rest():
    card_win.hide()
    n = box_min.value() * 60
    sleep(n)
    card_win.show()

def back_menu():
    card_win.hide()
    main_win.show()

def to_card():
    main_win.hide()
    card_win.show()

# підключаємо кнопки до функцій
btn_ok.clicked.connect(switch_screen)
btn_sleep.clicked.connect(rest)
btn_menu.clicked.connect(back_menu)
btn_back.clicked.connect(to_card)

card_win.show()
app.exec_()
