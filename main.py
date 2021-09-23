from Modelo import Fuzzy
from tkinter import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
import csv

print("teste parte inicial fuzzy")
print("teste 1, variaveis padrão")

fuzzy = Fuzzy(10)


def cria_valores():
    x = 1
    arquivo = open("valores.txt", "w")
    arquivo.truncate(0)
    for i in range(0, 100):
        x += round(randrange(-5, 10) / 10, 2)
        linha = str(x) + "\n"
        arquivo.write(linha)
    arquivo.close()


def teste():
    texto = fuzzy.mostra_parametros()
    label_parametros["text"] = texto
    calcula_fuzzy()
    graph()


def calcula_fuzzy():
    ia = 0
    valores = []
    dados = ""
    arquivo = open("valores.txt", "r")
    for linha in arquivo:
        valores.append(float(linha.strip()))
    arquivo.close()
    for i in valores:
        erro, derro = fuzzy.calcula_erro(i, ia)
        x, y = list(fuzzy.calcula_grau())
        ia = i
        dados = dados + f'''{x["MN"]},{x["N"]},{x["PN"]},{x["PP"]},{x["P"]},{x["MP"]},'''
        dados = dados + f'''{y["MN"]},{y["N"]},{y["PN"]},{y["PP"]},{y["P"]},{y["MP"]},'''
        dados = dados + f'''{erro},{derro}\n'''
    arquivo = open("resultados.txt", "w")
    arquivo.write(
        "erro_MN,erro_N,erro_PN,erro_PP,erro_P,erro_MP,Derro_MN,Derro_N,Derro_PN,,Derro_PP,Derro_P,Derro_MP,erro,derro\n")
    arquivo.write(dados)
    arquivo.close()


def graph():
    erro_MN, erro_N, erro_PN, erro_PP, erro_P, erro_MP, \
    Derro_MN, Derro_N, Derro_PN, Derro_PP, Derro_P, Derro_MP, \
    erro, derro = \
        [], [], [], [], [], [], [], [], [], [], [], [], [], []
    print("testando abrir arquivo em .csv")
    with open('resultados.txt') as arquivo:
        arquivo = csv.reader(arquivo, delimiter=',')
        for linha in arquivo:
            if 'erro_MN' in linha:
                pass
            else:
                erro_MN.append(float(linha[0]))
                erro_N.append(float(linha[1]))
                erro_PN.append(float(linha[2]))
                erro_PP.append(float(linha[3]))
                erro_P.append(float(linha[4]))
                erro_MP.append(float(linha[5]))
                Derro_MN.append(float(linha[6]))
                Derro_N.append(float(linha[7]))
                Derro_PN.append(float(linha[8]))
                Derro_PP.append(float(linha[9]))
                Derro_P.append(float(linha[10]))
                Derro_MP.append(float(linha[11]))
                erro.append(float(linha[12]))
                derro.append(float(linha[13]))
        print(erro_MN, "\n", erro_N, "\n", erro_PN, "\n", erro_PP, "\n", erro_P, "\n", erro_MP, "\n",
              Derro_MN, "\n", Derro_N, "\n", Derro_PN, "\n", Derro_PP, "\n", Derro_P, "\n", Derro_MP, "\n",
              erro, "\n", derro)
        y = [erro_MN, erro_N, erro_PN, erro_PP, erro_P, erro_MP]
        print(len(y[0]))
        i = 0
        valores = []
        arquivo = open("valores.txt", "r")
        for linha in arquivo:
            valores.append(float(linha.strip()))
        arquivo.close()
        for i in range(len(y)):
            plt.plot(valores, [x for x in y[i]], label='id %s' %i)
        # plt.plot(erro, erro_P, label='erro_P')
        # plt.show()
        # plt.plot([x for x in erro], [y for y in erro_MP], label='erro_MP')
        plt.show()


janela = Tk()
janela.geometry("400x400")
janela.title("teste fuzzy")

botao_iniciar = Button(janela, text="inciar fuzzy", command=teste)
botao_iniciar.grid(column=0, row=0, padx=10, pady=10)

botao_gerar_dados = Button(janela, text="Gerar dados", command=cria_valores)
botao_gerar_dados.grid(column=1, row=0, padx=10, pady=10)

label_parametros_titulo = Label(janela, text="parametro do fuzzy:")
label_parametros_titulo.grid(column=0, row=1, padx=0, pady=0)
label_parametros = Label(janela, text="")
label_parametros.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
