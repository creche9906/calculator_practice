import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        layout_equation_solution = QFormLayout()

# 수식 입력과 답 출력을 위한 라벨 생성
        label_equation = QLabel("")
        self.equation_solution = QLineEdit("")
        layout_equation_solution.addRow(label_equation, self.equation_solution)

#layout 생성
        layout_number = QGridLayout()
        layout_funtion = QGridLayout()


# 버튼 생성
        button_division = QPushButton("÷")
        button_multiply = QPushButton("x")
        button_minus = QPushButton("-")
        button_plus = QPushButton("+")
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")  
        button_clearE = QPushButton("CE")
        button_backspace = QPushButton("<-")  
        button_remainder = QPushButton("%")
        button_reciprocal = QPushButton("1/x")
        button_root = QPushButton("√")
        button_square = QPushButton("x^2")

        number_button_dict = {}
        for row in range(4):
            for col in range(3):
                number = row * 3 + col + 1
                number_button_dict[number] = QPushButton(str(number))
                number_button_dict[number].clicked.connect(lambda state, num=number:
                                                            self.number_button_clicked(num))
                layout_number.addWidget(number_button_dict[number], row, col)

        button_zero = QPushButton("0")
        button_dot = QPushButton(".")
        button_reverse = QPushButton("+/-")
        button_zero.clicked.connect(lambda state, num="0": self.number_button_clicked(num))
        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        button_reverse.clicked.connect(lambda state, num="-": self.number_button_clicked(num))

 # 버튼 레이아웃 추가
        layout_number.addWidget(button_reverse, 3, 0)
        layout_number.addWidget(button_zero, 3, 1)
        layout_number.addWidget(button_dot, 3, 2)
        layout_funtion.addWidget(button_division, 1, 3)
        layout_number.addWidget(button_multiply, 0, 3)
        layout_number.addWidget(button_minus, 1, 3)
        layout_number.addWidget(button_plus, 2, 3)
        layout_funtion.addWidget(button_remainder, 0, 0)
        layout_funtion.addWidget(button_clearE, 0, 1)
        layout_funtion.addWidget(button_clear, 0, 2)
        layout_funtion.addWidget(button_backspace, 0, 3)
        layout_funtion.addWidget(button_reciprocal, 1, 0)
        layout_funtion.addWidget(button_square, 1, 1)
        layout_funtion.addWidget(button_root, 1, 2)
        layout_number.addWidget(button_equal, 3, 3)

 # 버튼 눌렀을 때 기능 설정
        button_division.clicked.connect(lambda state, operation="/": self.button_operation_clicked(operation))
        button_multiply.clicked.connect(lambda state, operation="*": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation="-": self.button_operation_clicked(operation))
        button_plus.clicked.connect(lambda state, operation="+": self.button_operation_clicked(operation))
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clearE.clicked.connect(self.button_clearE_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_remainder.clicked.connect(lambda state, operation="%": self.button_operation_clicked(operation))

# 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addWidget(self.equation_solution)
        main_layout.addLayout(layout_funtion)
        main_layout.addLayout(layout_number)
        self.setLayout(main_layout)
        self.show()

    #################
# 계산기 기능에 관한 함수들 정의
        
    def number_button_clicked(self, num):
        equation = self.equation_solution.text()
        equation += str(num)
        self.equation_solution.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation_solution.text()
        equation += operation
        self.equation_solution.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation_solution.text()
        try:
            solution = str(eval(equation))
            self.equation_solution.setText(solution)
        except Exception as e:
            self.equation_solution.setText("Error")

    def button_clear_clicked(self):
        self.equation_solution.clear()

    def button_clearE_clicked(self):
        self.equation_solution.clear()

    def button_backspace_clicked(self):
        equation = self.equation_solution.text()
        equation = equation[:-1]
        self.equation_solution.setText(equation)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())