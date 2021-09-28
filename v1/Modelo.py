class Fuzzy:
    def __init__(self, setpoint):
        self.__setpoint = setpoint
        self.__parametros = [-10, -5, -1, 1, 5, 10]
        self.__erro_atual = 0
        self.__delta_erro = 0
        self.__grau_erro = {"MN": 0.0, "N": 0.0, "PN": 0.0, "PP": 0.0, "P": 0.0, "MP": 0.0}
        self.__grau_Drro = {"MN": 0.0, "N": 0.0, "PN": 0.0, "PP": 0.0, "P": 0.0, "MP": 0.0}

    def calcula_erro(self, valor_atual, valor_anterior):
        erro_atual = self.__setpoint - valor_atual
        erro_anterior = self.__setpoint - valor_anterior
        delta_erro = erro_atual - erro_anterior
        self.__erro_atual = erro_atual
        self.__delta_erro = delta_erro
        return self.__erro_atual, self.__delta_erro

    def __calcula_grau_erro(self):
        grau_1 = 0
        grau_2 = 0
        tipo_erro = []
        if self.__erro_atual <= self.__parametros[0]:
            MN = 1
            N = 0
            PN = 0
            PP = 0
            P = 0
            MP = 0
        elif self.__parametros[0] < self.__erro_atual <= self.__parametros[1]:
            A = self.__parametros[0]
            B = self.__parametros[1]
            erro = self.__erro_atual
            MN = (1 / (B - A)) * erro + (A / (A - B))
            N = (1 / (A - B)) * erro + (B / (B - A))
            PN = 0
            PP = 0
            P = 0
            MP = 0
        elif self.__parametros[1] < self.__erro_atual <= self.__parametros[2]:
            A = self.__parametros[1]
            B = self.__parametros[2]
            erro = self.__erro_atual
            MN = 0
            N = (1 / (B - A)) * erro + (A / (A - B))
            PN = (1 / (A - B)) * erro + (B / (B - A))
            PP = 0
            P = 0
            MP = 0
        elif self.__parametros[2] < self.__erro_atual <= self.__parametros[3]:
            A = self.__parametros[2]
            B = self.__parametros[3]
            erro = self.__erro_atual
            MN = 0
            N = 0
            PN = (1 / (B - A)) * erro + (A / (A - B))
            PP = (1 / (A - B)) * erro + (B / (B - A))
            P = 0
            MP = 0
        elif self.__parametros[3] < self.__erro_atual <= self.__parametros[4]:
            A = self.__parametros[3]
            B = self.__parametros[4]
            erro = self.__erro_atual
            MN = 0
            N = 0
            PN = 0
            PP = (1 / (B - A)) * erro + (A / (A - B))
            P = (1 / (A - B)) * erro + (B / (B - A))
            MP = 0
        elif self.__parametros[4] < self.__erro_atual < self.__parametros[5]:
            A = self.__parametros[4]
            B = self.__parametros[5]
            erro = self.__erro_atual
            MN = 0
            N = 0
            PN = 0
            PP = 0
            P = (1 / (B - A)) * erro + (A / (A - B))
            MP = (1 / (A - B)) * erro + (B / (B - A))
        elif self.__parametros[5] <= self.__erro_atual:
            MN = 0
            N = 0
            PN = 0
            PP = 0
            P = 0
            MP = 1
        self.__grau_erro["MN"] = MN
        self.__grau_erro["N"] = N
        self.__grau_erro["PN"] = PN
        self.__grau_erro["PP"] = PP
        self.__grau_erro["P"] = P
        self.__grau_erro["MP"] = MP

    def __calcula_grau_delta_erro(self):
        grau_1 = 1
        grau_2 = 0
        tipo_erro = []
        if self.__delta_erro <= self.__parametros[0]:
            MN = 1
            N = 0
            PN = 0
            PP = 0
            P = 0
            MP = 0
        elif self.__parametros[0] < self.__delta_erro <= self.__parametros[1]:
            A = self.__parametros[0]
            B = self.__parametros[1]
            erro = self.__erro_atual
            MN = (1 / (B - A)) + (A / (A - B))
            N = (1 / (A - B)) + (B / (B - A))
            PN = 0
            PP = 0
            P = 0
            MP = 0
        elif self.__parametros[1] < self.__delta_erro <= self.__parametros[2]:
            A = self.__parametros[1]
            B = self.__parametros[2]
            erro = self.__erro_atual
            MN = 0
            N = (1 / (B - A)) + (A / (A - B))
            PN = (1 / (A - B)) + (B / (B - A))
            PP = 0
            P = 0
            MP = 0
        elif self.__parametros[2] < self.__delta_erro <= self.__parametros[3]:
            A = self.__parametros[2]
            B = self.__parametros[3]
            erro = self.__erro_atual
            MN = 0
            N = 0
            PN = (1 / (B - A)) * erro + (A / (A - B))
            PP = (1 / (A - B)) * erro + (B / (B - A))
            P = 0
            MP = 0
        elif self.__parametros[3] < self.__delta_erro <= self.__parametros[4]:
            A = self.__parametros[3]
            B = self.__parametros[4]
            erro = self.__erro_atual
            MN = 0
            N = 0
            PN = 0
            PP = (1 / (B - A)) * erro + (A / (A - B))
            P = (1 / (A - B)) * erro + (B / (B - A))
            MP = 0
        elif self.__parametros[4] < self.__delta_erro < self.__parametros[5]:
            A = self.__parametros[4]
            B = self.__parametros[5]
            erro = self.__erro_atual
            MN = 0
            N = 0
            PN = 0
            PP = 0
            P = (1 / (B - A)) * erro + (A / (A - B))
            MP = (1 / (A - B)) * erro + (B / (B - A))
        elif self.__parametros[5] <= self.__delta_erro:
            MN = 0
            N = 0
            PN = 0
            PP = 0
            P = 0
            MP = 1
        self.__grau_Drro["MN"] = MN
        self.__grau_Drro["N"] = N
        self.__grau_Drro["PN"] = PN
        self.__grau_Drro["PP"] = PP
        self.__grau_Drro["P"] = P
        self.__grau_Drro["MP"] = MP

    def calcula_grau(self):
        self.__calcula_grau_erro()
        self.__calcula_grau_delta_erro()
        return self.__grau_erro, self.__grau_Drro

    def mostra_parametros(self):
        texto = [self.__parametros[0], self.__parametros[1],
                 self.__parametros[2], self.__parametros[3],
                 self.__parametros[4], self.__parametros[5]]
        text = f'''
            MN = {texto[0]}
            PN = {texto[1]}
            N = {texto[2]}
            P = {texto[3]}
            PP = {texto[4]}
            MP = {texto[5]}
            '''

        return text

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
