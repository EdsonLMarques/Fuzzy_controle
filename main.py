from Modelo import Fuzzy
print("teste parte inicial fuzzy")
print("teste 1, variaveis padrão")

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fuzzy = Fuzzy(10)
ia = 0
for i in valores:
    fuzzy.calcula_erro(i, ia)
    fuzzy.calcula_grau()
    ia = i
