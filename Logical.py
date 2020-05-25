import banco_de_dados_agua
vazoes_gas = {"c" : 9, "a": 15 , "b": 17, "m" : 16}
vazoes_eletrico = {"c" : 3, "a" : 9.6 , "b": 11.6, "m" : 10.6}
gasto_pessoa_semanal = []
gasto_pessoa_mensal = []
gasto_familia_mensal = []

def calculo_a_gas(tipo_house, minutos_pessoa,banhos_semanais, familia, minutos_familia):
    vazao = vazoes_gas[tipo_house]
    gasto_semanal = vazao * minutos_pessoa * banhos_semanais
    gasto_pessoa_semanal.append(gasto_semanal)
    gasto_mensal = gasto_semanal * 4
    gasto_pessoa_mensal.append(gasto_mensal)
    if familia > 0:
        familia_mensal = familia * minutos_familia * vazao * banhos_semanais * 4 + gasto_mensal
        gasto_familia_mensal.append(familia_mensal)

def calculo_eletrico(tipo_house, minutos_pessoa,banhos_semanais, familia, minutos_familia):
    vazao = vazoes_eletrico[tipo_house]
    gasto_semanal = vazao * minutos_pessoa * banhos_semanais
    gasto_pessoa_semanal.append(gasto_semanal)
    gasto_mensal = gasto_semanal * 4
    gasto_pessoa_mensal.append(gasto_mensal)
    if familia > 0:
        familia_mensal = familia * minutos_familia * vazao * banhos_semanais * 4 + gasto_mensal
        gasto_familia_mensal.append(familia_mensal)




print("""                    Seja bem vindo! 
Esse programa tem como objetivo mostrar ao usuário transparentemente seus gastos de água
e como isso pode afetar o mundo ;) """)
print("                     Vamos começar")


media_familia = 0
qnts_minutos = int(input("Quantos minutos em média você leva no banho? "))
qnts_banhos = int(input("Quantos banhos você toma em média por semana? "))
qnts_pessoas = int(input("Quantas pessoas moram com você? "))


if qnts_pessoas > 0:
    media_igual_a_familia = input(f"As pessoas da sua casa levam média {qnts_minutos} minutos por banho também? \n S= sim\n N= não \n ").lower()
    if media_igual_a_familia == "n":
        media_familia = int(input("Não? Então me conte... qual a média de sua familia?? \n"))
    else:
        media_familia = qnts_minutos


tipo_chuveiro = input("Hmm me diga, qual o tipo do seu chuveiro?\n E = para elétrico \n G = para á gás \n").lower()
while tipo_chuveiro != "e" and tipo_chuveiro != "g":
    print("Digitação inválida, tente novamente :/")
    tipo_chuveiro = input("Primeiro me diga, qual o tipo do seu chuveiro?\n E = para elétrico \n G = para á gás \n").lower()


casa_ou_ap = input("Você mora em casa ou apartamento? \n C= para casa \n A= para apartamento \n").lower()
while casa_ou_ap != "c" and casa_ou_ap != "a":
    print("Digitação inválida, tente novamente :/")
    casa_ou_ap = input("Você mora em casa ou apartamento? \n C= para casa \n A= para apartamento \n").lower()


if casa_ou_ap == "a":
    casa_ou_ap = input("Seu apartamento fica nos andares mais superiores, inferiores ou exatamente no meio? ? \n A= superiores \n B= inferiores \n M = meio \n").lower()
    while casa_ou_ap != "a" and casa_ou_ap != "b" and casa_ou_ap!= "m":
        print("Digitação inválida, tente novamente :/")
        casa_ou_ap = input("Seu apartamento fica nos andares mais superiores, inferiores ou exatamente no meio? ? \n A= superiores \n B= inferiores \n M = meio \n").lower()


if tipo_chuveiro == "g":
    calculo_a_gas(casa_ou_ap, qnts_minutos, qnts_banhos, qnts_pessoas, media_familia)
elif tipo_chuveiro == "e":
    calculo_eletrico(casa_ou_ap, qnts_minutos, qnts_banhos, qnts_pessoas, media_familia)


print("Analisando as informações que você forneceus, e considerando elas corretas:\n"
      f"VOCÊ gasta em aproximadamente {gasto_pessoa_semanal} litros de água POR SEMANA apenas tomando BANHO \n"
      f"E por mês aproximadamente {gasto_pessoa_mensal} litros!!! \n"
      f"E ainda tem mais, levando em conta que sua familia tome a mesma quantidade de banhos que você por semana, \n"
      f"na sua casa o gasto POR MÊS apenas com banho é de {gasto_familia_mensal} litros de água")


