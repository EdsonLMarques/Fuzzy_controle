class Fuzzy:
    def __init__(self, setpoint):
        self.__setpoint = setpoint
        self.__parametros = [-10, -5, -1, 1, 5, 10]
        self.__erro_atual = 0
        self.__delta_erro = 0

    def calcula_erro(self, valor_atual, valor_anterior):
        erro_atual = self.__setpoint - valor_atual
        erro_anterior = self.__setpoint - valor_anterior
        delta_erro = erro_atual - erro_anterior
        self.__erro_atual = erro_atual
        self.__delta_erro = delta_erro
        print("erro = {}\nerro_anterior = {}\nresultando em um delta erro = {}".format(self.__erro_atual, erro_anterior,  self.__delta_erro))
        return self.__erro_atual, self.__delta_erro

    def __calcula_grau_erro(self):
        grau_1 = 0
        grau_2 = 0
        tipo_erro = []
        print(self.__parametros)
        if self.__erro_atual <= self.__parametros[0]:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MN"]
        elif self.__parametros[0] < self.__erro_atual <= self.__parametros[1]:
            A = self.__parametros[0]
            B = self.__parametros[1]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["MN", "N"]
        elif self.__parametros[1] < self.__erro_atual <= self.__parametros[2]:
            A = self.__parametros[1]
            B = self.__parametros[2]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["N", "PN"]
        elif self.__parametros[2] < self.__erro_atual <= self.__parametros[3]:
            A = self.__parametros[2]
            B = self.__parametros[3]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["PN", "PP"]
        elif self.__parametros[3] < self.__erro_atual <= self.__parametros[4]:
            A = self.__parametros[3]
            B = self.__parametros[4]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["PP", "P"]
        elif self.__parametros[4] < self.__erro_atual < self.__parametros[5]:
            A = self.__parametros[4]
            B = self.__parametros[5]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["P", "MP"]
        elif self.__parametros[5] <= self.__erro_atual:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MP"]
        print("grau_1_E = {}   grau_2_E= {}   tipo_E= {}".format(grau_1, grau_2, tipo_erro))
        return grau_1, grau_2, tipo_erro

    def __calcula_grau_delta_erro(self):
        grau_1 = 1
        grau_2 = 0
        tipo_erro = []
        if self.__delta_erro <= self.__parametros[0]:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MN"]
        elif self.__parametros[0] < self.__delta_erro <= self.__parametros[1]:
            A = self.__parametros[0]
            B = self.__parametros[1]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["MN", "N"]
        elif self.__parametros[1] < self.__delta_erro <= self.__parametros[2]:
            A = self.__parametros[1]
            B = self.__parametros[2]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["N", "PN"]
        elif self.__parametros[2] < self.__delta_erro <= self.__parametros[3]:
            A = self.__parametros[2]
            B = self.__parametros[3]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["PN", "PP"]
        elif self.__parametros[3] < self.__delta_erro <= self.__parametros[4]:
            A = self.__parametros[3]
            B = self.__parametros[4]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["PP", "P"]
        elif self.__parametros[4] < self.__delta_erro < self.__parametros[5]:
            A = self.__parametros[4]
            B = self.__parametros[5]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["P", "MP"]
        elif self.__parametros[5] <= self.__delta_erro:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MP"]
        print("grau_1_DE = {}   grau_2_DE= {}   tipo_DE= {}".format(grau_1, grau_2, tipo_erro))
        return grau_1, grau_2, tipo_erro

    def calcula_grau(self):
        # try:
            # calcular grau 1 e 2 do erro
            self.__calcula_grau_erro()
            #calcula grau 1 e 2 do delta erro
            self.__calcula_grau_delta_erro()
        # except:
        #     print("ERRO")

    def mostra_parametros(self):
        print(self.__parametros[0])
        print(self.__parametros[1])
        print(self.__parametros[2])
        print(self.__parametros[3])
        print(self.__parametros[4])
        print(self.__parametros[5])
    @property
    def setpoint(self):
        print(self.__setpoint)
        return self.__setpoint

    @setpoint.setter
    def setpoint(self, novo_setpoint):
        self.__setpoint = novo_setpoint

    @staticmethod
    def parametros_padrao():
        print("-10, -5, -1, 1, 5, 10")
