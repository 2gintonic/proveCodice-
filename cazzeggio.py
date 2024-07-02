contatti = {}

contatti["alberto"] = 3455433234

numero = contatti.get(str(input("nome del contatto?")))

print(f"il numero del contatto scelto è: {numero}")