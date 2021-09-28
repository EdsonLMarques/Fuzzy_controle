class Simple_Fuzzy:

    def __init__(self):
        self.grau = [0, 0, 0, 0, 0, 0]
        self.grau_saida = [0, 0, 0, 0, 0, 0]
        self.saida = 0
        self.parametros_entrada = [-10, -5, -1, 1, 5, 10]
        self.parametros_saida = [0, 25, 50, 75, 100]
        self.base = [["MB", "B", "M", "M", "A", "MA"]]

    def calcula_fuzzy(self, valor):
        grau = self.calcula_grau(valor)
        saida = self.calcula_saida(grau)
        return saida

    def calcula_grau(self, valor):
        MN, N, PN, PP, P, MP = self.parametros_entrada
        grau = [0, 0, 0, 0, 0, 0]
        if valor <= MN:
            grau[0] = 1
        elif MN < valor <= N:
            A = MN
            B = N
            grau[0] = (1 / (B - A)) * valor + (A / (A - B))
            grau[1] = (1 / (A - B)) * valor + (B / (B - A))
        elif N < valor <= PN:
            A = N
            B = PN
            grau[1] = (1 / (B - A)) * valor + (A / (A - B))
            grau[2] = (1 / (A - B)) * valor + (B / (B - A))
        elif PN < valor <= PP:
            A = PN
            B = PP
            grau[2] = (1 / (B - A)) * valor + (A / (A - B))
            grau[3] = (1 / (A - B)) * valor + (B / (B - A))
        elif PP < valor <= P:
            A = PP
            B = P
            grau[3] = (1 / (B - A)) * valor + (A / (A - B))
            grau[4] = (1 / (A - B)) * valor + (B / (B - A))
        elif P < valor <= MP:
            A = P
            B = MP
            grau[4] = (1 / (B - A)) * valor + (A / (A - B))
            grau[5] = (1 / (A - B)) * valor + (B / (B - A))
        else:
            grau[5] = 1
            return grau

    def calcula_saida(self, grau):
        # base
        # Base =
        # base = grau
        # saida
        pass

    def get_grau(self):
        return self.grau

    def get_grau_saida(self):
        return self.get_grau_saida

    def saida(self):
        return self.saida

    def set_parametros_entrada(self, parametros):
        self.parametros_entrada = parametros