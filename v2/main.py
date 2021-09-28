#simple fuzzy that defines how much something is
#
#



from fuzzy import Simple_Fuzzy

fuzzy = Simple_Fuzzy()
for i in range(-11,11):
    saida = fuzzy.calcula_fuzzy(i)
print(saida)
