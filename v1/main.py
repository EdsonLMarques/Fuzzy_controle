from tkinter import *
from Modelo import Fuzzy
from random import *

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
    fuzzy = Fuzzy(10)
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
    pass

print("teste parte inicial fuzzy")
print("teste 1, variaveis padrão")

fuzzy = Fuzzy(10)

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