import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Gabriel') # renomeando a janela
        self.setFixedSize(400,400) # fica a janela em um unico tamanho
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True) #Estou desativando o comentario
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px}' #estou configurando a cor e a fonte
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding) # o sizepolicy se expandindo de acordo com  o espaço na janela

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #59C173; color: #fff; font-weight: 700;'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: #a17fe0; color: #fff; font-weight: 700;'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1)
        self.add_btn(QPushButton('/'), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton('('), 4, 2, 1, 1)
        self.add_btn(QPushButton(')'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #5D26C1; color: #fff; font-weight: 700;'
        )

        self.setCentralWidget(self.cw) # estou setando o central com o cw

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None): # esse metodo vai adicionar botão
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(  # quando clicar no botão, ele venha adicionar o valor ao display
                lambda: self.display.setText(  # enviando informação ao display
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style) #enviando cor para botão

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # expandindo o botão dos numeros

    def eval_igual(self): #função para o botão de igual
        try:
            self.display.setText( #estou avaliando se a conta é valida
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Inválida')


if __name__=='__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
