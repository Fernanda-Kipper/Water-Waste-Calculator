
#Janela Principal, início do programa

from PyQt5 import QtCore, QtGui, QtWidgets
#Importando a outra parte do programa, que contém a próxima janela e a lógica
from app_janela_perguntas import Ui_janela2_1perg

class Ui_janela(object):

    def AbrirJanelas(self):
        #Função que irá chamar a próxima janela(e última, por que depois ela só é atualizada, mudando os objetos que ela está pritando)
        # que será usada nesse programa
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_janela2_1perg()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def setupUi(self, janela):
        # Função própia do Qt Designer, declarando os objetos que serão usados(botões, caixas de texto.. )
        janela.setObjectName("janela")
        janela.resize(1080, 500)
        janela.setStyleSheet("background-color:rgb(180, 239, 255)")
        self.janelacentral = QtWidgets.QWidget(janela)
        self.janelacentral.setObjectName("janelacentral")

        self.label_boas_vindas = QtWidgets.QLabel(self.janelacentral)
        self.label_boas_vindas.setGeometry(QtCore.QRect(390, 20, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_boas_vindas.setFont(font)
        self.label_boas_vindas.setObjectName("label_boas_vindas")

        self.label_texto_intro = QtWidgets.QLabel(self.janelacentral)
        self.label_texto_intro.setGeometry(QtCore.QRect(210, 80, 801, 141))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_texto_intro.setFont(font)
        self.label_texto_intro.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_texto_intro.setObjectName("label_texto_intro")

        self.label_explicando = QtWidgets.QLabel(self.janelacentral)
        self.label_explicando.setGeometry(QtCore.QRect(210, 230, 771, 161))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(16)
        self.label_explicando.setFont(font)
        self.label_explicando.setObjectName("label_explicando")

        self.botaoStart = QtWidgets.QPushButton(self.janelacentral)
        self.botaoStart.setGeometry(QtCore.QRect(460, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(False)
        font.setWeight(50)
        self.botaoStart.setFont(font)
        self.botaoStart.setObjectName("botaoStart")
        self.botaoStart.clicked.connect(self.AbrirJanelas)

        self.owner_name = QtWidgets.QLabel(self.janelacentral)
        self.owner_name.setGeometry(QtCore.QRect(610, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(11)
        self.owner_name.setFont(font)
        self.owner_name.setObjectName("owner_name")

        janela.setCentralWidget(self.janelacentral)
        self.menubar = QtWidgets.QMenuBar(janela)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 18))
        self.menubar.setObjectName("menubar")
        self.menuWaterCountDown = QtWidgets.QMenu(self.menubar)
        self.menuWaterCountDown.setObjectName("menuWaterCountDown")
        janela.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(janela)
        self.statusbar.setObjectName("statusbar")
        janela.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuWaterCountDown.menuAction())

        self.retranslateUi(janela)
        QtCore.QMetaObject.connectSlotsByName(janela)

    def retranslateUi(self, janela):
        # Função própia do Qt Designer, que traduz para a forma de ui o que será escrito nos objetos
        _translate = QtCore.QCoreApplication.translate
        janela.setWindowTitle(_translate("janela", "WaterCountDown"))
        self.label_boas_vindas.setText(_translate("janela", " Seja Bem Vindo!   "))
        self.label_texto_intro.setText(_translate("janela", "Esse programa tem como objetivo abrir seus olhos a respeito do uso da água \n"
"  e em como isso pode afetar o mundo... \n"
" E para fazer isso, resolvemos fazer um simples cálculo para você."))
        self.label_explicando.setText(_translate("janela", "Vai funcionar assim:\n"
" A partir de algumas informaçoes que você vai nos fornecer, \n"
"  vamos calcular seus gasto semanal e mensal de água apenas para tomar banho "))
        self.botaoStart.setText(_translate("janela", "Começar"))
        self.owner_name.setText(_translate("janela", "Feito por: Fernanda Kipper"))
        self.menuWaterCountDown.setTitle(_translate("janela", "ContandoGastos.Agua"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = QtWidgets.QMainWindow()
    ui = Ui_janela()
    ui.setupUi(janela)
    janela.show()
    sys.exit(app.exec_())
