#Dicionários que contêm os valores das vazões para cada tipo de chuveiro e tipagem de moradia
# c= casa; a = apartamento andares superiores; m = apartamento andares médios ; b = apartamento andares inferiores
vazoes_gas = {"c" : 9, "a": 15 , "b": 17, "m" : 16}
vazoes_eletrico = {"c" : 3, "a" : 9.6 , "b": 11.6, "m" : 10.6}

#Declarando váriaveis que serão utilizadas posteriormente para armazenar o resultado dos cálculos
gasto_pessoa_semanal = []
gasto_pessoa_mensal = []
gasto_familia_mensal = []


#Declarando funções que serão utilizadas posteriormente para armazenar as informações fornecidas pelo usuário
valor_tempo_banho = []
respostas_da_spin_box = []
banhos_por_semana = []
familia = []
valor_tempo_banho_familia = []
tipo_chuveiro = []
tipo_casa = []

def calculo_a_gas(tipo_house, minutos_pessoa,banhos_semanais, familia, minutos_familia):
    #Função que calcula os gastos para um chuveiro á gás
    vazao = vazoes_gas[tipo_house]
    gasto_semanal = vazao * minutos_pessoa * banhos_semanais
    gasto_pessoa_semanal.append(gasto_semanal)
    gasto_mensal = gasto_semanal * 4
    gasto_pessoa_mensal.append(gasto_mensal)
    if familia > 0:
        familia_mensal = familia * minutos_familia * vazao * banhos_semanais * 4 + gasto_mensal
        gasto_familia_mensal.append(familia_mensal)

def calculo_eletrico(tipo_house, minutos_pessoa,banhos_semanais, familia, minutos_familia):
    #Função que calcula os gastos um chuveiro elétrico
    vazao = vazoes_eletrico[tipo_house]
    gasto_semanal = vazao * minutos_pessoa * banhos_semanais
    gasto_pessoa_semanal.append(gasto_semanal)
    gasto_mensal = gasto_semanal * 4
    gasto_pessoa_mensal.append(gasto_mensal)
    if familia > 0:
        familia_mensal = familia * minutos_familia * vazao * banhos_semanais * 4 + gasto_mensal
        gasto_familia_mensal.append(familia_mensal)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janela2_1perg(object):
    def setupUi(self, janela2_1perg):
        #Função própia do Qt Designer, declarando os objetos que serão usados(botões, caixas de texto.. )
        janela2_1perg.setObjectName("janela2_1perg")
        janela2_1perg.setEnabled(True)
        janela2_1perg.resize(1080, 500)
        janela2_1perg.setStyleSheet("background-color:rgb(180, 239, 255)")

        self.pergunta1 = QtWidgets.QLabel(janela2_1perg)
        self.pergunta1.setGeometry(QtCore.QRect(350, 100, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.pergunta1.setFont(font)
        self.pergunta1.setObjectName("pergunta1")

        self.label = QtWidgets.QLabel(janela2_1perg)
        self.label.setGeometry(QtCore.QRect(200, 120, 101, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("relogio1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.minutosbanho = QtWidgets.QSpinBox(janela2_1perg)
        self.minutosbanho.valueChanged.connect(self.ValueBanho)
        self.minutosbanho.setGeometry(QtCore.QRect(420, 270, 191, 41))
        self.minutosbanho.setObjectName("minutosbanho")

        self.pushButton = QtWidgets.QPushButton(janela2_1perg)
        self.pushButton.setGeometry(QtCore.QRect(470, 370, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Update1)

        self.ButtonSim = QtWidgets.QPushButton(janela2_1perg)
        self.ButtonSim.setGeometry(QtCore.QRect(390, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ButtonSim.setFont(font)
        self.ButtonSim.setObjectName("ButtonSim")
        self.ButtonSim.hide()

        self.ButtonNao = QtWidgets.QPushButton(janela2_1perg)
        self.ButtonNao.setGeometry(QtCore.QRect(510, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ButtonNao.setFont(font)
        self.ButtonNao.setObjectName("ButtonNao")
        self.ButtonNao.hide()

        self.ButtonGas = QtWidgets.QPushButton(janela2_1perg)
        self.ButtonGas.setGeometry(QtCore.QRect(390, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ButtonGas.setFont(font)
        self.ButtonGas.setObjectName("ButtonGas")
        self.ButtonGas.hide()

        self.ButtonEletrico = QtWidgets.QPushButton(janela2_1perg)
        self.ButtonEletrico.setGeometry(QtCore.QRect(510, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ButtonEletrico.setFont(font)
        self.ButtonEletrico.setObjectName("ButtonEletrico")
        self.ButtonEletrico.hide()

        self.ButtonCasa = QtWidgets.QPushButton(janela2_1perg)
        self.ButtonCasa.setGeometry(QtCore.QRect(390, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ButtonCasa.setFont(font)
        self.ButtonCasa.setObjectName("ButtonCasa")
        self.ButtonCasa.hide()

        self.ButtonApto = QtWidgets.QPushButton(janela2_1perg)
        self.ButtonApto.setGeometry(QtCore.QRect(510, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ButtonApto.setFont(font)
        self.ButtonApto.setObjectName("ButtonApto")
        self.ButtonApto.hide()

        self.AptoSuperior = QtWidgets.QCheckBox(janela2_1perg)
        self.AptoSuperior.setGeometry(QtCore.QRect(350, 245, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.AptoSuperior.setFont(font)
        self.AptoSuperior.setObjectName("Check Apto Superior")
        self.AptoSuperior.hide()

        self.AptoMedio = QtWidgets.QCheckBox(janela2_1perg)
        self.AptoMedio.setGeometry(QtCore.QRect(350, 280, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.AptoMedio.setFont(font)
        self.AptoMedio.setObjectName("Check Apto Medio")
        self.AptoMedio.hide()

        self.AptoInferior= QtWidgets.QCheckBox(janela2_1perg)
        self.AptoInferior.setGeometry(QtCore.QRect(350,315, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.AptoInferior.setFont(font)
        self.AptoInferior.setObjectName("Check Apto Inferiorr")
        self.AptoInferior.hide()

        self.retranslateUi(janela2_1perg)
        QtCore.QMetaObject.connectSlotsByName(janela2_1perg)

    def ValueBanho(self):
        #Função que adiciona o último valor alterado da spin box à lista de valores spin box
         self.valor_minutos_banho = self.minutosbanho.value()
         respostas_da_spin_box.append(self.valor_minutos_banho)



    def Update1(self):
        #Função que adiciona à lista que contêm o tempo que ao usuário leva no banho
        # o seu valor[0] -> e único
        #Página que pergunta ao usuário quanto tempo ele leva no banho
        valor_tempo_banho.append(respostas_da_spin_box[-1])
        self.ButtonSim.hide()
        self.ButtonNao.hide()
        self.pergunta1.setText("Quantos banhos por semana você toma?")
        self.label.setPixmap(QtGui.QPixmap("chuveiro.png"))
        self.pushButton.clicked.connect(self.Update2)

    def Update2(self):
        #Função que adiciona à lista de quantidade de banhos p/ semana o seu valor[0] -> e único
        #Página que pergunta ao usuário quantas pessoas vivem na sua casa
        banhos_por_semana.append(respostas_da_spin_box[-1])
        self.ButtonSim.hide()
        self.ButtonNao.hide()
        self.pergunta1.setText("Quantas pessoas moram com você? ")
        self.label.setPixmap(QtGui.QPixmap("familia.png"))
        self.pushButton.clicked.connect(self.Update3)


    def Update3(self):
        #Função que adiciona á lista de integrantes da familia o seu valor [0] -> e único
        #Página que pergunta se as pessoas que moram com a pessoa/usuário levam o mesmo tempo de banho
        #Só é chamada se a resposta do update2 for "x > 0 ... maior que zero "
        familia.append(respostas_da_spin_box[-1])
        if familia[0] > 0:
            self.pergunta1.setText("As pessoas de sua casa levam o mesmo\n tempo no banho que você??")
            self.ButtonNao.show()
            self.ButtonSim.show()
            self.minutosbanho.hide()
            self.pushButton.hide()

            self.ButtonSim.clicked.connect(self.Update4)
            self.ButtonNao.clicked.connect(self.Update5)
        else:
            self.Update6()

    def Update4(self):
        #Função que adiciona á lista de contagem do tempo do banho da familia
        # o seu valor [0] -> único valor -> e igual ao da pessoa/usuário
        valor_tempo_banho_familia.append(valor_tempo_banho[0])
        self.Update6()

    def Update5(self):
        #Página que pergunta ao usuário o valor que corresponde ao tempo dos familiares no banho
        #Só é chamada se a resposta do update3 for "não"
        self.pergunta1.setText("Não?... \n Então qual o tempo deles? ")
        self.ButtonNao.hide()
        self.ButtonSim.hide()
        self.minutosbanho.show()
        self.pushButton.show()
        self.pushButton.clicked.connect(self.Update6)


    def Update6(self):
        #Função que adiciona à lista de contagem de minutos do tempo da familia (diferente do valor da pessoa/usuário )
        # o seu valor [0]  -> único valor
        #Página que pergunta ao usuário a tipagem de chuveiro
        valor_tempo_banho_familia.append(respostas_da_spin_box[-1])
        self.pergunta1.setText("Hmm, então me diga, \n Qual o tipo de chuveiro\n na sua casa?? ")
        self.label.setPixmap(QtGui.QPixmap("chuveiro.png"))
        self.ButtonSim.hide()
        self.ButtonNao.hide()
        self.minutosbanho.hide()
        self.pushButton.hide()
        self.ButtonEletrico.show()
        self.ButtonGas.show()

        self.ButtonEletrico.clicked.connect(self.Update7)
        self.ButtonGas.clicked.connect(self.Update8)

    def Update7(self):
        #Função que adiciona à lista de tipagem de chuveiro a configuração "elétrico"
        tipo_chuveiro.append("e")
        self.Update9()

    def Update8(self):
        #Função que adiciona à lista de tipagem de chuveiro a configuração "gás"
        tipo_chuveiro.append("g")
        self.Update9()

    def Update9(self):
        #Página que pergunta ao usuário o tipo de moradia
        self.ButtonGas.hide()
        self.ButtonEletrico.hide()
        self.ButtonApto.show()
        self.ButtonCasa.show()
        self.pergunta1.setText("Você mora em casa ou apto?")
        self.label.setPixmap(QtGui.QPixmap("casa.png"))
        self.ButtonApto.clicked.connect(self.Update10)
        self.ButtonCasa.clicked.connect(self.Update11)

    def Update10(self):
        #Página que pergunta ao usuário a posição/configuração do apartamento
        #Só é chamada se a resposta do update9 for "apto"
        self.pergunta1.setText("Qual a posição do seu apartamento em \n relação ao prédio inteiro? \n Obs: check apenas um! ")
        self.ButtonApto.hide()
        self.ButtonCasa.hide()
        self.AptoSuperior.show()
        self.AptoInferior.show()
        self.AptoMedio.show()
        self.pushButton.show()
        self.pushButton.clicked.connect(self.Update12)

    def Update11(self):
        #Função que adiciona à lista da tipagem da moradia a informaçao de ser casa
        # E então chama a página final
        tipo_casa.append("c")
        if tipo_chuveiro[0] == "g":
            calculo_a_gas(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0],
                          valor_tempo_banho_familia[0])
        elif tipo_chuveiro[0] == "e":
            calculo_eletrico(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0],
                             valor_tempo_banho_familia[0])
        self.Update13()


    def Update12(self):
        #Função que adiciona à lista da tipagem da moradia, qual a configuração do apartamento da pessoa
        # E então chama a pagina final
        if self.AptoSuperior.checkState() == 2:
            tipo_casa.append("a")
            if tipo_chuveiro[0] == "g":
                calculo_a_gas(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0], valor_tempo_banho_familia[0])
            elif tipo_chuveiro[0] == "e":
                calculo_eletrico(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0], valor_tempo_banho_familia[0])
            self.Update13()

        elif self.AptoMedio.checkState() == 2:
            tipo_casa.append("m")
            if tipo_chuveiro[0] == "g":
                calculo_a_gas(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0], valor_tempo_banho_familia[0])
            elif tipo_chuveiro[0] == "e":
                calculo_eletrico(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0], valor_tempo_banho_familia[0])
            self.Update13()

        elif self.AptoInferior.checkState() == 2:
            tipo_casa.append("b")
            if tipo_chuveiro[0] == "g":
                calculo_a_gas(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0], valor_tempo_banho_familia[0])
            elif tipo_chuveiro[0] == "e":
                calculo_eletrico(tipo_casa[0], valor_tempo_banho[0], banhos_por_semana[0], familia[0], valor_tempo_banho_familia[0])
            self.Update13()
        else:
            self.Update9()

    def Update13(self):
        #Página final, mostrandos os resultados
        self.pergunta1.setGeometry(QtCore.QRect(50, 0, 910, 550))
        self.pergunta1.setText("Analisando as informações que você forneceu,\n"
                               f"VOCÊ gasta em aproximadamente {gasto_pessoa_semanal} litros de água POR SEMANA no BANHO \n"
                               f"E por mês aproximadamente {gasto_pessoa_mensal} litros!!! \n"
                               f"E tem mais, levando em conta que sua familia \n "
                               f"tome a mesma quantia de banhos que você p/ semana, \n"
                               f"Na sua casa o gasto POR MÊS apenas com banho é de {gasto_familia_mensal} litros de água")
        self.ButtonApto.hide()
        self.ButtonCasa.hide()
        self.AptoInferior.hide()
        self.AptoMedio.hide()
        self.AptoSuperior.hide()
        self.pushButton.hide()
        self.label.hide()
        self.ButtonGas.hide()
        self.ButtonEletrico.hide()
        self.ButtonSim.hide()
        self.ButtonNao.hide()

    def retranslateUi(self, janela2_1perg):
        # Função própia do Qt Designer, que traduz para a forma de ui o que será escrito nos objetos
        _translate = QtCore.QCoreApplication.translate
        janela2_1perg.setWindowTitle(_translate("janela2_1perg", "Descubrindo o gasto de água"))
        self.pergunta1.setText(_translate("janela2_1perg", "Quantos minutos em média você leva no banho?"))
        self.pushButton.setText(_translate("janela2_1perg", "Próximo"))
        _translate = QtCore.QCoreApplication.translate
        self.ButtonSim.setText(_translate("janela2_1perg", "Sim"))
        self.ButtonNao.setText(_translate("janela2_1perg", "Não"))
        self.ButtonGas.setText(_translate("janela2_1perg", "Ducha/Gás"))
        self.ButtonEletrico.setText(_translate("janela2_1perg", "Elétrico"))
        self.ButtonCasa.setText(_translate("janela2_1perg", "Casa"))
        self.ButtonApto.setText(_translate("janela2_1perg", "Apartamento"))
        self.AptoSuperior.setText(_translate("janela2_1perg", "Superior"))
        self.AptoMedio.setText(_translate("janela2_1perg", "No meio"))
        self.AptoInferior.setText(_translate("janela2_1perg", "Inferior"))

if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    janela2_1perg = QtWidgets.QWidget()
    ui = Ui_janela2_1perg()
    ui.setupUi(janela2_1perg)
    janela2_1perg.show()
    sys.exit(app.exec_())


