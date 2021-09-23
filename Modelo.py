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
        self.__erro_anterior = delta_erro
        print("erro = {}\nerro_anterior = {}\nresultando em um delta erro = {}".format(self.__erro_atual, erro_anterior,  self.__erro_anterior))
        return self.__erro_atual, self.__delta_erro

    def __calcula_grau_erro(self):
        if self.__erro_atual < self.__parametros[0]:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MN"]
        elif self.__parametros[0] < self.__erro_atual < self.__parametros[1]:
            A = self.__parametros[0]
            B = self.__parametros[1]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["MN", "N"]
        elif self.__parametros[1] < self.__erro_atual < self.__parametros[2]:
            A = self.__parametros[1]
            B = self.__parametros[2]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["N", "PN"]
        elif self.__parametros[2] < self.__erro_atual < self.__parametros[3]:
            A = self.__parametros[2]
            B = self.__parametros[3]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["PN", "PP"]
        elif self.__parametros[3] < self.__erro_atual < self.__parametros[4]:
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
        elif self.__parametros[5] < self.__erro_atual:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MP"]
        return grau_1, grau_2, tipo_erro

    def __calcula_grau_delta_erro(self):
        if self.__delta_erro < self.__parametros[0]:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MN"]
        elif self.__parametros[0] < self.__delta_erro < self.__parametros[1]:
            A = self.__parametros[0]
            B = self.__parametros[1]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["MN", "N"]
        elif self.__parametros[1] < self.__delta_erro < self.__parametros[2]:
            A = self.__parametros[1]
            B = self.__parametros[2]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["N", "PN"]
        elif self.__parametros[2] < self.__delta_erro < self.__parametros[3]:
            A = self.__parametros[2]
            B = self.__parametros[3]
            grau_1 = (1 / (B - A)) + (A / (A - B))
            grau_2 = (1 / (A - B)) + (B / (B - A))
            tipo_erro = ["PN", "PP"]
        elif self.__parametros[3] < self.__delta_erro < self.__parametros[4]:
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
        elif self.__parametros[5] < self.__delta_erro:
            grau_1 = 1
            grau_2 = 0
            tipo_erro = ["MP"]
        return grau_1, grau_2, tipo_erro

    def calcula_grau(self):
        try:
            # calcular grau 1 e 2 do erro
            grau_1_E, grau_2_E, tipo_E = Fuzzy.__calcula_grau_erro(self)
            #calcula grau 1 e 2 do delta erro
            grau_1_DE, grau_2_DE, tipo_DE = Fuzzy.__calcula_grau_delta_erro(self)
            print("grau_1_E = {}   grau_2_E= {}   tipo_E= {}".format(grau_1_E, grau_2_E, tipo_E))
            print("grau_1_DE = {}   grau_2_DE= {}   tipo_DE= {}".format(grau_1_DE, grau_2_DE, tipo_DE))
        except:
            return "ERRO"

    @property
    def setpoint(self):
        print(self.__setpoint)
        return self.__setpoint

    @setpoint.setter
    def setpoint(self, novo_setpoint):
        self.__setpoint = novo_setpoint

    @staticmethod
    def parametros_padrao():
        return ("-10, -5, -1, 1, 5, 10")
