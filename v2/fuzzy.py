class Simple_Fuzzy:

    def __init__(self):
        self.grau = [0, 0, 0, 0, 0, 0]
        self.grau_saida = [0, 0, 0, 0, 0, 0]
        self.saida = 0
        self.parametros_entrada = [-10, -5, -1, 1, 5, 10]
        self.parametros_saida = [0, 25, 50, 75, 100]
        self.base = ["MB", "B", "M", "A", "MA", "MA"]

    def calcula_fuzzy(self, valor):
        self.calcula_grau(valor)
        saida = self.calcula_saida()
        print(f'''saida = {saida}\n\n''')
        return saida

    def calcula_grau(self, valor):
        MN, N, PN, PP, P, MP = self.parametros_entrada
        grau = [0, 0, 0, 0, 0, 0]
        if valor < MN:
            grau[0] = 1
        elif MN <= valor < N:
            A = MN
            B = N
            grau[1] = (1 / (B - A)) * valor + (A / (A - B))
            grau[0] = (1 / (A - B)) * valor + (B / (B - A))
        elif N <= valor < PN:
            A = N
            B = PN
            grau[2] = (1 / (B - A)) * valor + (A / (A - B))
            grau[1] = (1 / (A - B)) * valor + (B / (B - A))
        elif PN <= valor < PP:
            A = PN
            B = PP
            grau[3] = (1 / (B - A)) * valor + (A / (A - B))
            grau[2] = (1 / (A - B)) * valor + (B / (B - A))
        elif PP <= valor < P:
            A = PP
            B = P
            grau[4] = (1 / (B - A)) * valor + (A / (A - B))
            grau[3] = (1 / (A - B)) * valor + (B / (B - A))
        elif P <= valor <= MP:
            A = P
            B = MP
            grau[5] = (1 / (B - A)) * valor + (A / (A - B))
            grau[4] = (1 / (A - B)) * valor + (B / (B - A))
        elif valor > MP:
            grau[5] = 1
        self.grau = grau
        return grau

    def calcula_saida(self):
        base = self.base
        grau = self.grau
        matriz = zip(base, grau)
        matriz = list(matriz)
        MB = []
        B = []
        M = []
        A = []
        MA = []
        for item in matriz:
            if item[0] == "MB":
                MB.append(item[1])
            elif item[0] == "B":
                B.append(item[1])
            elif item[0] == "M":
                M.append(item[1])
            elif item[0] == "A":
                A.append(item[1])
            elif item[0] == "MA":
                MA.append(item[1])
        MB = max(MB)
        B = max(B)
        M = max(M)
        A = max(A)
        MA = max(MA)
        grau_saida = [MB, B, M, A, MA]
        parametros_saidas = self.parametros_saida
        print(f'''grau saida = {grau_saida}''')
        try: #rever essa formmula
            saida = ((parametros_saidas[0]+1) * MB + (parametros_saidas[1]) * B +
                     (parametros_saidas[2]) * M + (parametros_saidas[3]) * A +
                     (parametros_saidas[4]) * MA) \
                    / (MB + B + M + A + MA)
            self.grau_saida = grau_saida
            self.saida = saida
            return saida
        except:
            print("divisão por 0")

    def get_grau(self):
        return self.grau

    def get_grau_saida(self):
        return self.get_grau_saida

    def get_saida(self):
        return self.saida

    def set_parametros_entrada(self, parametros):
        self.parametros_entrada = parametros